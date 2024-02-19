from django.test import TestCase
from django.utils import timezone
from main.models import Medicine
from users.models import Comment, User
from users.services import add_to_favourites


class UserModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='testuser', password='testpassword')
        cls.medicine1 = Medicine.objects.create(name='Medicine 1', price=10.0)
        cls.medicine2 = Medicine.objects.create(name='Medicine 2', price=15.0)

    def test_get_fav_list(self):
        self.user.favourites.add(self.medicine1, self.medicine2)
        fav_list = self.user.get_fav_list()
        self.assertEqual(len(fav_list), 2)
        self.assertIn(self.medicine1.id, fav_list)
        self.assertIn(self.medicine2.id, fav_list)

    def test_get_cart_list(self):
        self.user.cart.add(self.medicine1, self.medicine2)
        cart_list = self.user.get_cart_list()
        self.assertEqual(len(cart_list), 2)
        self.assertIn(self.medicine1.id, cart_list)
        self.assertIn(self.medicine2.id, cart_list)

    def test_user_str(self):
        self.assertEqual(str(self.user), 'testuser')

    @classmethod
    def tearDownClass(cls):
        # Clean up created objects
        cls.user.delete()
        cls.medicine1.delete()
        cls.medicine2.delete()


class CommentModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='testuser', password='testpassword')
        cls.medicine = Medicine.objects.create(name='Test Medicine', price=10.0)

    def test_comment_str(self):
        comment = Comment.objects.create(user=self.user, medicine=self.medicine, comment='Test Comment', date_posted=timezone.now())
        self.assertEqual(str(comment), f'Коментарій користувача {self.user} про препарат {self.medicine}')

    @classmethod
    def tearDownClass(cls):
        # Clean up created objects
        cls.user.delete()
        cls.medicine.delete()


class AddToFavouritesTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='testuser', password='testpassword')
        cls.medicine = Medicine.objects.create(name='Test Medicine', price=10.0)

    def test_add_to_favourites_adds_medicine(self):
        add_to_favourites(username='testuser', medicine_id=self.medicine.id)
        self.assertTrue(self.medicine in self.user.favourites.all())

    def test_add_to_favourites_removes_medicine(self):
        self.user.favourites.add(self.medicine)
        add_to_favourites(username='testuser', medicine_id=self.medicine.id)
        self.assertFalse(self.medicine in self.user.favourites.all())

    @classmethod
    def tearDownClass(cls):
        # Clean up created objects
        cls.user.delete()
        cls.medicine.delete()
