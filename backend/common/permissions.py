from rest_framework import permissions


class IsOwnerOrSupport(permissions.BasePermission):
    """
    Object-level permission to only allow owners or support access.
    """

    def has_object_permission(self, request, view, obj):
        return obj.user.id == request.user.id
