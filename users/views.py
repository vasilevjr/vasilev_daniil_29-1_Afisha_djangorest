from rest_framework import generics
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from .serializers import AuthorizationValidateSerializer, RegistrationValidateSerializer, ClientSerializer
from django.contrib.auth.models import User
from .models import Client
from rest_framework.views import APIView


@api_view(['POST'])
def registration_api_view(request):
    serializer = RegistrationValidateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    username = serializer.validated_data.get('username')
    password = serializer.validated_data.get('password')

    user = User.objects.create_user(username=username, password=password, is_active=False)

    client = Client.objects.create(user=user)

    response_data = {
        'user_id': user.id,
        'client_code': client.code,
        'username': user.username,
    }

    return Response(status=201, data=response_data)


class AthorizationAPIView(APIView):
    def post(self, request):
        serializer = AuthorizationValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data.get('username')
        password = serializer.validated_data.get('password')
        code = serializer.validated_data.get('code')
        user = authenticate(username=username, password=password, is_active=False)

        if user is not None and user.client.code == code:
            token_, created = Token.objects.get_or_create(user=user)
            return Response(data={'key': token_.key})

        return Response(status=401, data={'message': 'Invalid credentials or code'})
