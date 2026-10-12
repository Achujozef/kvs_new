import re

from django.core.paginator import Paginator
from django.db.models import Q

PER_PAGE = 50


def _search_terms(q):
    """The text as typed, plus a phone-number form ("+91 99-95 48" -> "999548")
    so numbers match however they were typed or stored."""
    terms = [q]
    digits = re.sub(r'[\s\-().]', '', q)
    if digits.startswith('+'):
        digits = digits[1:]
    if digits.isdigit() and len(digits) > 10 and digits.startswith('91'):
        digits = digits[2:]
    if digits.isdigit() and digits != q:
        terms.append(digits)
    return terms


def paginate(request, queryset, search_fields=(), per_page=PER_PAGE):
    """Filter ``queryset`` by the ``q`` GET param over ``search_fields`` and
    return ``(page_obj, q)``. ``page_obj`` is iterable like the queryset and
    carries what ``partials/pagination.html`` needs."""
    q = request.GET.get('q', '').strip()
    if queryset is None:
        queryset = []
    elif q and search_fields:
        condition = Q()
        for term in _search_terms(q):
            for field in search_fields:
                condition |= Q(**{f'{field}__icontains': term})
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
