from django.contrib.auth import authenticate

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND

    
class LoginView(APIView):
    def post(self, request, format=None):
        data = request.data

        username = data.get('username', None)
        password = data.get('password', None)

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                return Response(status=HTTP_200_OK)
            else:
                return Response(status=HTTP_404_NOT_FOUND)
        else:
            return Response(status=HTTP_404_NOT_FOUND)
