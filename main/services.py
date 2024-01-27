from .models import Medicine, Categories, Forms, CountryOfOrigin, UserInfo
from django.contrib.auth.models import User


def check_authenticated(context: dict, user) -> dict:
    """ Checks if a user is authenticated and updates the context accordingly. """

    if user.is_authenticated:
        context['current_user'] = {'username': user.username,
                                   'favourites': list(UserInfo.objects.get(user=user)
                                                      .favourites.all().values_list('id', flat=True))}
    return context


def get_info_for_filters(medicines) -> dict:
    """ Retrieves information for constructing filters on the site. """

    filters = {
        'categories': Categories.objects.values_list('id', 'name'),
        'forms': Forms.objects.values_list('id', 'name'),
        'countries': CountryOfOrigin.objects.values_list('id', 'name'),
        'param_list': "category, form, country, prescription",
        }

    if medicines:
        filters['min_price'] = medicines.order_by('price').first().price
        filters['max_price'] = medicines.order_by('price').last().price

    return filters


def search_medicines(req=None, search_by_id=False) -> dict:
    """ Search for medicines based on various filters. """

    if search_by_id:
        return {'medicine': Medicine.objects.filter(id=search_by_id).first()}

    return {'medicines': Medicine.filter_medicines(
                            search=req.GET.get('search', ''),
                            price_range=(req.GET.get('minp', 0),
                                         req.GET.get('maxp', Medicine.objects.order_by('price').last().price)),
                            category=req.GET.getlist('category', [str(i) for i in range(20)]),
                            form=req.GET.getlist('form', [str(i) for i in range(20)]),
                            country=req.GET.getlist('country', [str(i) for i in range(20)]),
                            prescription=req.GET.getlist('prescription', [0, 1]),
                            )
            }


def get_info_for_user_page(username) -> dict:
    """ Retrieves information for displaying a user page. """

    user = User.objects.filter(username=username).first()

    if not user:
        return False

    user_info = UserInfo.objects.get_or_create(user=user)
    return {'user_about': user, 'add_info': user_info}


def add_to_favourites(username, medicine_id):
    user = UserInfo.objects.get(user=User.objects.filter(username=username).first())
    medicine = Medicine.objects.get(id=medicine_id)

    if medicine in user.favourites.all():
        user.favourites.remove(Medicine.objects.get(id=medicine_id))
    else:
        user.favourites.add(Medicine.objects.get(id=medicine_id))
