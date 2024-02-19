from django.test import TestCase
from users.models import User
from main.models import Medicine
from .services import add_to_cart


class AddToCartTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.medicine = Medicine.objects.create(name='Test Medicine', price=10.0)

    def test_add_to_cart(self):
        initial_cart_count = self.user.cart.count()

        # Add medicine to cart
        add_to_cart(username=self.user.username, medicine_id=self.medicine.id)
        self.assertEqual(self.user.cart.count(), initial_cart_count + 1)

        # Add same medicine again (should remove it from cart)
        add_to_cart(username=self.user.username, medicine_id=self.medicine.id)
        self.assertEqual(self.user.cart.count(), initial_cart_count)

    def test_add_to_cart_invalid_medicine_id(self):
        # Try to add medicine with invalid medicine_id
        with self.assertRaises(Medicine.DoesNotExist):
            add_to_cart(username=self.user.username, medicine_id=9999)

    def test_add_to_cart_invalid_username(self):
        # Try to add medicine with invalid username
        with self.assertRaises(User.DoesNotExist):
            add_to_cart(username='invalidusername', medicine_id=self.medicine.id)

    def tearDown(self):
        self.user.delete()
        self.medicine.delete()
