from django.test import TestCase
from ..models import Medicine, Category, Form, CountryOfOrigin
from users.models import Comment, User
from ..services import get_info_for_filters, search_medicines, add_comment, delete_comment, get_all_comments_about_medicine


class MedicineServicesTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create sample data for testing
        cls.category = Category.objects.create(name='Test Category')
        cls.form = Form.objects.create(name='Test Form')
        cls.country_of_origin = CountryOfOrigin.objects.create(name='Test Country')

        cls.medicine1 = Medicine.objects.create(
            name='Medicine 1',
            price=10.0,
            category=cls.category,
            form=cls.form,
            country_of_origin=cls.country_of_origin,
            is_prescription_required=False,
            date_of_manufacture='2022-01-01',
            service_life=24,
            description='Test Description',
            quantity=100
        )

        cls.user = User.objects.create(username='testuser')

    def test_get_info_for_filters(self):
        # Test when there are no medicines
        filters = get_info_for_filters(medicines=None)
        self.assertEqual(filters['categories'].count(), 1)
        self.assertEqual(filters['forms'].count(), 1)
        self.assertEqual(filters['countries'].count(), 1)
        self.assertEqual(filters['param_list'], "category, form, country, prescription")
        self.assertIsNone(filters.get('min_price'))
        self.assertIsNone(filters.get('max_price'))

        # Test when there are medicines
        filters = get_info_for_filters(medicines=Medicine.objects.all())
        self.assertIsNotNone(filters.get('min_price'))
        self.assertIsNotNone(filters.get('max_price'))

    def test_search_medicines(self):
        # Test searching by ID
        result = search_medicines(search_by_id=self.medicine1.id)
        self.assertIn('medicine', result)

    def test_add_comment(self):
        # Test adding a comment
        add_comment(username='testuser', medicine=self.medicine1, comment='Test Comment')
        self.assertEqual(Comment.objects.filter(user=self.user, medicine=self.medicine1, comment='Test Comment').count(), 1)

    def test_delete_comment(self):
        # Create a comment to be deleted
        comment = Comment.objects.create(user=self.user, medicine=self.medicine1, comment='Test Comment')

        # Test deleting a comment
        delete_comment(comment_id=comment.id)
        self.assertEqual(Comment.objects.filter(id=comment.id).count(), 0)

    def test_get_all_comments_about_medicine(self):
        # Create some comments
        Comment.objects.create(user=self.user, medicine=self.medicine1, comment='Test Comment 1')
        Comment.objects.create(user=self.user, medicine=self.medicine1, comment='Test Comment 2')

        # Test retrieving all comments about a medicine
        comments = get_all_comments_about_medicine(medicine=self.medicine1)
        self.assertEqual(comments.count(), 2)

    @classmethod
    def tearDownClass(cls):
        # Clean up created objects
        cls.category.delete()
        cls.form.delete()
        cls.country_of_origin.delete()
        cls.medicine1.delete()
        cls.user.delete()
