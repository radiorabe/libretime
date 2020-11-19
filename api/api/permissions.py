from rest_framework.permissions import IsAdminUser, BasePermission

class IsOwnUser(BasePermission):
    def has_permission(self, request, view):
        # Permission only makes sense at an object level
        return False

    def has_object_permission(self, request, view, obj):
        return obj.username == request.user
