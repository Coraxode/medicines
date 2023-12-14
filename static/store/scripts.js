function change_param(param, cat_id) {
    const url = new URL(window.location.href);
    const paramValues = url.searchParams.getAll(param);
    const catIdString = cat_id.toString();

    if (paramValues.includes(catIdString) && paramValues.length === 1) {
        url.searchParams.delete(param);
    } else if (paramValues.includes(catIdString)) {
        const filteredValues = paramValues.filter(value => value !== catIdString);
        url.searchParams.delete(param);
        filteredValues.forEach(value => url.searchParams.append(param, value));
    } else {
        url.searchParams.append(param, catIdString);
    }

    window.location.href = url.href;
}

