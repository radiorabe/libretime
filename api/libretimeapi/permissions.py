from rest_framework.permissions import IsAdminUser, BasePermission
from django.conf import settings

class IsOwnUser(BasePermission):
    def has_permission(self, request, view):
        # Permission only makes sense at an object level
        return False

    def has_object_permission(self, request, view, obj):
        return obj.username == request.user

class IsSystemToken(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True

        auth_header = request.META.get('Authorization')
        if not auth_header:
            auth_header = request.META.get('HTTP_AUTHORIZATION', '')

        if auth_header.startswith('Api-Key'):
            token = auth_header.split()[1]
            if token == settings.CONFIG.get('general', 'api_key'):
                return True
        return False
