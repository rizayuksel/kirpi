from kirpi.trailers.models import Trailer

from rest_framework.serializers import ModelSerializer


class ListTrailersSerializer(ModelSerializer):

    class Meta:
        model = Trailer
        fields = [
            "id",
            "serial_number",
            "last_t0",
            "last_t1",
            "last_t2",
            "last_t3",
            "last_ri",
            "last_rc",
            "t0",
            "t1",
            "t2",
            "t3",
            "ri",
            "rc",
            "price",
            "last_date",
            "date",
        ]


class DetailTrailerSerializer(ModelSerializer):

    class Meta:
        model = Trailer
        fields = [
            "id",
            "serial_number",
            "last_t0",
            "last_t1",
            "last_t2",
            "last_t3",
            "last_ri",
            "last_rc",
            "t0",
            "t1",
            "t2",
            "t3",
            "ri",
            "rc",
            "price",
            "last_date",
            "date",
        ]
