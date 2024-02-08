function change_param(param, cat_id, change_name_or_price=null) {
    const url = new URL(window.location.href);
    const paramValues = url.searchParams.getAll(param);
    const catIdString = cat_id.toString();

    if (param == 'order_by') {
        url.searchParams.delete(param);
        url.searchParams.set(param, cat_id);

        return window.location.href = url.href;
    }

    if (change_name_or_price !== null) {
        if (change_name_or_price == '') {
            url.searchParams.delete(param);
        } else {
            url.searchParams.set(param, change_name_or_price);
        }
        
        return window.location.href = url.href;
    }

    if (paramValues.includes(catIdString) && paramValues.length === 1) {
        url.searchParams.delete(param);
    } else if (paramValues.includes(catIdString)) {
        const filteredValues = paramValues.filter(value => value !== catIdString);
        url.searchParams.delete(param);
        filteredValues.forEach(value => url.searchParams.append(param, value));
    } else {
        url.searchParams.append(param, catIdString);
    }

    return window.location.href = url.href;
}

function set_filters(param_list) {
    param_list = param_list.split(', ');
    const url = new URL(window.location.href);

    if (url.searchParams.get('search')) document.getElementById('search').value = url.searchParams.get('search');
    if (url.searchParams.get('minp')) document.getElementById('minp').value = url.searchParams.get('minp');
    if (url.searchParams.get('maxp')) document.getElementById('maxp').value = url.searchParams.get('maxp');

    for (let i = 0; i < param_list.length; i += 1) {
        const params = url.searchParams.getAll(param_list[i]);
        params.forEach((element) => document.getElementById(param_list[i] + '_' + element).checked = true);
    }
}

function add_search_event() {
    ['search', 'minp', 'maxp'].forEach((param) => {
        document.getElementById(param).addEventListener('keypress', function (e) {
            if (e.key === 'Enter') {
                change_param(param, 0, document.getElementById(param).value);
            }
        });
    })
}

function check_is_in_favourites_and_cart(favourites_list, cart_list) {
    for (let i = 0; i < favourites_list.length; i++) {
        btn = document.getElementById("add-to-favourites-button-" + favourites_list[i]);
        if (btn) {
            btn.value = "В улюблених";
            btn.style.backgroundColor = "orange";
        }
    }

    for (let i = 0; i < cart_list.length; i++) {
        btn = document.getElementById("add-to-cart-button-" + cart_list[i]);
        if (btn) {
            btn.value = "В корзині";
            btn.style.backgroundColor = "green";
        }
    }
}
