
from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsSuperUser(BasePermission):
    """
    Restricts access to superusers.
    """
    message = "This action is restricted to superusers."

    def has_permission(self, request, view):
        return (
            request.user and request.user.is_authenticated
            and request.user.is_superuser
        )


class IsAuthorizedContributorOrReadOnly(BasePermission):
    """
    Restricts access to authorized contributors.
    """

    def has_permission(self, request, view):
        is_allowed = False
        is_authenticated = request.user and request.user.is_authenticated
        if is_authenticated and request.user.hiker.is_contributor:
            is_allowed = True
        return bool(request.method in SAFE_METHODS or is_allowed)


class IsHikerOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        is_owner = False
        obj_hiker = getattr(obj, 'hiker', None)
        if request.user and request.user.is_authenticated:
            hiker = request.user.hiker
            if obj_hiker == hiker:
                is_owner = True
        return is_owner