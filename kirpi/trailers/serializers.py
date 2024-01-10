from kirpi.trailers.models import Trailer

from rest_framework.serializers import ModelSerializer


class ListTrailersSerializer(ModelSerializer):

    class Meta:
        model = Trailer
        fields = [
            "id",
            "name",
            "created_at",
        ]

class DetailTrailerSerializer(ModelSerializer):

    class Meta:
        model = Trailer
        fields = [
            "id",
            "name",
            "created_at",
        ]