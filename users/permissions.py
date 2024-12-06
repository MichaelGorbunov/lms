from rest_framework.permissions import BasePermission


class IsModerator(BasePermission):
    """Проверяет, является ли пользователь модератором."""

    def has_permission(self, request, view):
        return request.user.groups.filter(name="Moderators").exists()


class IsOwner(BasePermission):
    """Проверяет, является ли пользователь владельцем курса/урока."""

    def has_object_permission(self, request, view, obj):
        if request.user == obj.owner:
            return True
        return False


