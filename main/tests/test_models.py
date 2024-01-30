from django.test import TestCase
from django.contrib.auth.models import User
from ..models import Category, Form, Manufacturer, CountryOfOrigin, Medicine


class MedicineModelTest(TestCase):
    def setUp(self):
        category = Category.objects.create(name='Протизастудні')
        form = Form.objects.create(name='Таблетки')
        manufacturer = Manufacturer.objects.create(name='Manufacturer1')
        country = CountryOfOrigin.objects.create(name='Country1')

        self.medicine = Medicine.objects.create(
            name='Medicine1',
            price=10.5,
            date_of_manufacture='2023-01-01',
            service_life=12,
            description='Description',
            quantity=100,
        )

        self.medicine.category.set([category])
        self.medicine.form.set([form])
        self.medicine.manufacturer.set([manufacturer])
        self.medicine.country_of_origin.set([country])
        self.medicine.save()

    def test_medicine_str_method(self):
        self.assertEqual(str(self.medicine), 'Medicine1')

    def test_filter_medicines_method(self):
        result = Medicine.filter_medicines(
            search='Medicine1',
            price_range=(10, 20),
            category=[1],
            form=[1],
            country=[1],
            prescription=[False]
        )
        self.assertEqual(result.count(), 1)


class UserInfoModelTest(TestCase):
    def setUp(self):
        # Попередня налаштування для тестів
        user = User.objects.create(username='testuser')
        medicine = Medicine.objects.create(name='TestMedicine')

        self.user_info.favourites.add(medicine)

    def test_user_info_str_method(self):
        self.assertEqual(str(self.user_info), 'testuser info')

    def test_user_info_favourites(self):
        favourites = self.user_info.favourites.all()
        self.assertEqual(favourites.count(), 1)
        self.assertEqual(favourites[0].name, 'TestMedicine')
