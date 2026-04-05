from .membership_utils import get_membership_fee_total_cached


def membership_fee_total(request):
    """Expose renewal fee sum in all templates (cached; safe for public display)."""
    return {'membership_fee_total': get_membership_fee_total_cached()}
