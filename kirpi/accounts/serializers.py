from django.contrib.auth.models import User
from django.utils.translation import gettext as _

from rest_framework.serializers import ModelSerializer


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "username",
        ]
