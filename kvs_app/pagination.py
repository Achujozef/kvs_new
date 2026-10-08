from django.core.paginator import Paginator
from django.db.models import Q

PER_PAGE = 50


def paginate(request, queryset, search_fields=(), per_page=PER_PAGE):
    """Filter ``queryset`` by the ``q`` GET param over ``search_fields`` and
    return ``(page_obj, q)``. ``page_obj`` is iterable like the queryset and
    carries what ``partials/pagination.html`` needs."""
    q = request.GET.get('q', '').strip()
    if queryset is None:
        queryset = []
    elif q and search_fields:
        condition = Q()
        for field in search_fields:
            condition |= Q(**{f'{field}__icontains': q})
        queryset = queryset.filter(condition)

    paginator = Paginator(queryset, per_page)
    page_obj = paginator.get_page(request.GET.get('page'))
    page_obj.page_window = list(
        paginator.get_elided_page_range(page_obj.number, on_each_side=2, on_ends=1)
    )
    params = request.GET.copy()
    params.pop('page', None)
    page_obj.qs_base = params.urlencode()
    return page_obj, q
