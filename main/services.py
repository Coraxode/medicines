from .models import Medicine, Category, Form, CountryOfOrigin


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
                            order_by=req.GET.get('order_by', 'id')
                            )
            }
