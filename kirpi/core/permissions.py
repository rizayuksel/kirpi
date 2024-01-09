from kirpi.core.types import AuthenticatedRequest

from rest_framework.permissions import BasePermission
from rest_framework.views import APIView

class KirpiIsAuthenticated(BasePermission):
    def has_permission(self, request: AuthenticatedRequest, view: APIView) -> bool:
        return bool(request.user and request.user.is_authenticated)
