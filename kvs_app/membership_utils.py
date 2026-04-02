from decimal import Decimal

from django.core.cache import cache
from django.db.models import Sum


MEMBERSHIP_FEE_TOTAL_CACHE_KEY = 'kvs_membership_renewal_amount_total'


def get_membership_fee_total_cached():
    """Sum of MembershipRenewal.amount; cached briefly for navbar/dashboard."""
    from .models import MembershipRenewal

    cached = cache.get(MEMBERSHIP_FEE_TOTAL_CACHE_KEY)
    if cached is not None:
        return Decimal(cached)
    agg = MembershipRenewal.objects.aggregate(total=Sum('amount'))
    raw = agg['total'] or Decimal('0')
    cache.set(MEMBERSHIP_FEE_TOTAL_CACHE_KEY, str(raw), 300)
    return raw


def invalidate_membership_fee_total_cache():
    cache.delete(MEMBERSHIP_FEE_TOTAL_CACHE_KEY)
