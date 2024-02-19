from django.test import TestCase
from ..models import Medicine, Category, Form, Manufacturer, CountryOfOrigin


class MedicineModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create sample data for testing
        cls.category = Category.objects.create(name='Test Category')
        cls.form = Form.objects.create(name='Test Form')
        cls.manufacturer = Manufacturer.objects.create(name='Test Manufacturer')
        cls.country_of_origin = CountryOfOrigin.objects.create(name='Test Country')

        # Create sample medicines
        cls.medicine1 = Medicine.objects.create(
            name='Medicine1',
            price=10.0,
            category=cls.category,
            form=cls.form,
            manufacturer=cls.manufacturer,
            country_of_origin=cls.country_of_origin,
            is_prescription_required=False,
            date_of_manufacture='2022-01-01',
            service_life=24,
            description='Test Description',
            quantity=100
        )
        cls.medicine2 = Medicine.objects.create(
            name='Medicine2',
            price=15.0,
            category=cls.category,
            form=cls.form,
            manufacturer=cls.manufacturer,
            country_of_origin=cls.country_of_origin,
            is_prescription_required=True,
            date_of_manufacture='2022-01-01',
            service_life=12,
            description='Test Description 2',
            quantity=50
        )

    def test_filter_medicines(self):
        # Test filtering without any criteria
        filtered_medicines = Medicine.filter_medicines(
            search="",
            price_range=(0, 1000),
            category=[self.category],
            form=[self.form],
            country=[self.country_of_origin],
            prescription=[False],
            order_by="price",
        )
        self.assertEqual(filtered_medicines.count(), 1)
        self.assertIn(self.medicine1, filtered_medicines)

        # Test filtering with prescription required criteria
        filtered_medicines = Medicine.filter_medicines(
            search="",
            price_range=(0, 1000),
            category=[self.category],
            form=[self.form],
            country=[self.country_of_origin],
            prescription=[True],
            order_by="price",
        )
        self.assertEqual(filtered_medicines.count(), 1)
        self.assertIn(self.medicine2, filtered_medicines)

        # Test filtering with price range criteria
        filtered_medicines = Medicine.filter_medicines(
            search="",
            price_range=(0, 10),
            category=[self.category],
            form=[self.form],
            country=[self.country_of_origin],
            prescription=[False],
            order_by="price",
        )
        self.assertEqual(filtered_medicines.count(), 1)
        self.assertIn(self.medicine1, filtered_medicines)

        # Test filtering with multiple criteria
        filtered_medicines = Medicine.filter_medicines(
            search="",
            price_range=(0, 1000),
            category=[self.category],
            form=[self.form],
            country=[self.country_of_origin],
            prescription=[False],
            order_by="price",
        )
        self.assertEqual(filtered_medicines.count(), 1)
        self.assertIn(self.medicine1, filtered_medicines)

    @classmethod
    def tearDownClass(cls):
        # Clean up created objects
        cls.category.delete()
        cls.form.delete()
        cls.manufacturer.delete()
        cls.country_of_origin.delete()
        cls.medicine1.delete()
        cls.medicine2.delete()
