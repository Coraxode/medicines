from .models import User
from main.models import Medicine


def add_to_favourites(username, medicine_id) -> None:
    user = User.objects.get(username=username)
    medicine = Medicine.objects.get(id=medicine_id)

    if medicine in user.favourites.all():
        user.favourites.remove(medicine)
    else:
        user.favourites.add(medicine)
