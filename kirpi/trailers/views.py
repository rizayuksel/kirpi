from typing import TYPE_CHECKING

from kirpi.trailers.models import Trailer
from kirpi.trailers.serializers import DetailTrailerSerializer, ListTrailersSerializer

from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED
from rest_framework.views import APIView

if TYPE_CHECKING:
    from django.db.models.query import QuerySet


class ListCreateTrailersView(ListCreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = ListTrailersSerializer

    def get_queryset(self) -> "QuerySet[Trailer]":
        return Trailer.objects.filter(is_active=True).order_by("-created_at")

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.check_object_permissions(request, self)
        serializer.save()

        return Response(data=serializer.data, status=HTTP_201_CREATED)


class DetailTrailerView(RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = DetailTrailerSerializer

    def get_queryset(self) -> "QuerySet[Trailer]":
        return Trailer.objects.filter(id=self.kwargs["pk"])


class TrailerCountView(APIView):
    def get(self, request, format=None):
        trailer_count = Trailer.objects.filter(is_active=True).count()
        return Response({"trailer_count": trailer_count}, status=HTTP_200_OK)
