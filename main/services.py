from .models import Medicine, Category, Form, CountryOfOrigin
from users.models import Comment, User


def get_info_for_filters(medicines) -> dict:
    """ Retrieves information for constructing filters on the site. """

    filters = {
        'categories': Category.objects.values_list('id', 'name'),
        'forms': Form.objects.values_list('id', 'name'),
        'countries': CountryOfOrigin.objects.values_list('id', 'name'),
        'param_list': "category, form, country, prescription",
    }

    if medicines:
        filters['min_price'] = medicines.order_by('price').first().price
        filters['max_price'] = medicines.order_by('price').last().price

    return filters


def search_medicines(request=None, search_by_id=False) -> dict:
    """ Search for medicines based on various filters. """

    if search_by_id:
        return {'medicine': Medicine.objects.filter(id=search_by_id).first()}

    return {'medicines': Medicine.filter_medicines(
        search=request.GET.get('search', ''),
        price_range=(request.GET.get('minp', 0),
                     request.GET.get('maxp', Medicine.objects.order_by('price').last().price)),
        category=request.GET.getlist('category', [str(i) for i in range(20)]),
        form=request.GET.getlist('form', [str(i) for i in range(20)]),
        country=request.GET.getlist('country', [str(i) for i in range(20)]),
        prescription=request.GET.getlist('prescription', [0, 1]),
        order_by=request.GET.get('order_by', 'id')
    )}


def add_comment(username, medicine, comment):
    user = User.objects.get(username=username)
    Comment.objects.create(user=user, medicine=medicine, comment=comment)


def delete_comment(comment_id):
    Comment.objects.get(id=comment_id).delete()


def get_all_comments_about_medicine(medicine):
    return Comment.objects.filter(medicine=medicine).order_by('-date_posted')
