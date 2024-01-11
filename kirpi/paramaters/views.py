from typing import TYPE_CHECKING

from kirpi.paramaters.models import Price
from kirpi.paramaters.serializers import PriceSerializer

from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny

if TYPE_CHECKING:
    from django.db.models.query import QuerySet

class PriceView(RetrieveUpdateAPIView):
    permission_classes = [AllowAny]
    serializer_class = PriceSerializer

    def get_queryset(self) -> "QuerySet[Price]":
        return Price.objects.all()
