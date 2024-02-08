from main.models import Medicine
from users.services import get_user_by_username


def add_to_cart(username, medicine_id):
    user = get_user_by_username(username)
    medicine = Medicine.objects.get(id=medicine_id)
    
    if medicine in user.cart.all():
        user.cart.remove(medicine)
    else:
        user.cart.add(medicine)
