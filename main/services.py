from .models import Medicine, Categories, Forms, CountryOfOrigin, UserInfo
from django.contrib.auth.models import User


def check_authenticated(context: dict, user) -> dict:
    """ Checks if a user is authenticated and updates the context accordingly. """

    if user.is_authenticated:
        context['current_user'] = {'username': user.username}

    return context


def get_info_for_filters() -> dict:
    """ Retrieves information for constructing filters on the site. """

    return {
        'categories': Categories.objects.values_list('id', 'name'),
        'forms': Forms.objects.values_list('id', 'name'),
        'countries': CountryOfOrigin.objects.values_list('id', 'name'),
        'min_price': Medicine.objects.order_by('price').first().price,
        'max_price': Medicine.objects.order_by('price').last().price,
        'param_list': "category, form, country, prescription",
        }


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
