from hikers.models import Hiker


def deleted_hiker_fallback():
    empty_user, created = Hiker.objects.get_or_create(
        hiker='deleted_user@hiketheplanet')
    return empty_user
