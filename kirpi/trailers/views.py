from typing import TYPE_CHECKING

from kirpi.trailers.models import Trailer
from kirpi.trailers.serializers import ListTrailersSerializer, DetailTrailerSerializer

from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny

if TYPE_CHECKING:
    from django.db.models.query import QuerySet


class ListTrailersView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = ListTrailersSerializer

    def get_queryset(self) -> "QuerySet[Trailer]":
        return Trailer.objects.filter(is_active=True).order_by("-created_at")


class DetailTrailerView(RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = DetailTrailerSerializer

    def get_queryset(self) -> "QuerySet[Trailer]":
        return Trailer.objects.filter(id=self.kwargs["pk"])
