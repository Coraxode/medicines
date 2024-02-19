from main.models import Medicine
from users.models import User


def add_to_cart(username, medicine_id):
    user = User.objects.get(username=username)
    medicine = Medicine.objects.get(id=medicine_id)
    
    if medicine in user.cart.all():
        user.cart.remove(medicine)
    else:
        user.cart.add(medicine)
