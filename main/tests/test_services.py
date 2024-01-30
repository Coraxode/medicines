from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from ..models import Medicine, Category, Form, CountryOfOrigin
from ..services import get_info_for_filters, search_medicines


class YourAppTestCase(TestCase):
    def setUp(self):
        # Set up necessary objects for testing
        self.user = User.objects.create(username='testuser', password='testpassword')
        self.category = Category.objects.create(name='TestCategory')
        self.form = Forms.objects.create(name='TestForm')
        self.country = CountryOfOrigin.objects.create(name='TestCountry')
        self.medicine = Medicine.objects.create(
            name='TestMedicine',
            price=10.5,
        )
        self.user_info = UserInfo.objects.create(user=self.user)

        self.medicine.category.set([self.category])
        self.medicine.form.set([self.form])
        self.medicine.country_of_origin.set([self.country])

    def test_check_authenticated(self):
        # Test for the check_authenticated function
        context = check_authenticated({}, self.user)
        self.assertEqual(context['current_user']['username'], 'testuser')

    def test_get_info_for_filters(self):
        # Test for the get_info_for_filters function
        filters = get_info_for_filters(Medicine.objects.all())
        self.assertEqual(filters['categories'][0][1], 'TestCategory')

    def test_search_medicines(self):
        # Test for the search_medicines function
        request_factory = RequestFactory()
        request_mock = request_factory.get('/store/', {'search': 'TestMedicine'})
        result = search_medicines(req=request_mock)
        self.assertEqual(result['medicines'].count(), 1)

    def test_get_info_for_user_page(self):
        # Test for the get_info_for_user_page function
        result = get_info_for_user_page('testuser')
        self.assertEqual(result['user_about'].username, 'testuser')

    def test_add_to_favourites(self):
        # Test for the add_to_favourites function
        add_to_favourites('testuser', self.medicine.id)
        self.assertEqual(self.user_info.favourites.count(), 1)

        add_to_favourites('testuser', self.medicine.id)  # Remove from favorites
        self.assertEqual(self.user_info.favourites.count(), 0)
