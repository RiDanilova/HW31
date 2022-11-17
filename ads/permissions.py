from rest_framework import permissions

from users.models import UserRoles


class IsOwnerSelection(permissions.BasePermission):
    message = "Нет прав на изменение подборки!"

    def has_object_permission(self, request, view, obj):
        if request.user == obj.owner:
            return True
        return False


class IsOwnerOrStaffAd(permissions.BasePermission):
    message = "Нет прав на изменение объявления!"

    def has_object_permission(self, request, view, obj):
        if request.user == obj.owner or request.user.role in [UserRoles.ADMIN, UserRoles.MODERATOR]:
            return True
        return False
