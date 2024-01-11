from kirpi.paramaters.models import Price

from rest_framework.serializers import ModelSerializer


class PriceSerializer(ModelSerializer):

    class Meta:
        model = Price
        fields = [
            "id",
            "price",
            "updated_at",
        ]