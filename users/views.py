from random import random

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .forms import RegistrationForm
from .serializers import RegisterValidateSerializer, AuthorizeValidateSerializer


@api_view(['POST'])
def register_api_view(request):
    serializer = RegisterValidateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    username = serializer.validated_data.get('username')
    password = serializer.validated_data.get('password')

    User.objects.create_user(username=username, password=password, is_active=False)
    return Response(status=201)


@api_view(['POST'])
def authorize_api_view(request):
    serializer = AuthorizeValidateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    user = authenticate(**serializer.validated_data)

    if user:
        token, _ = Token.objects.get_or_create(user=user)
        return Response(data={'key': token.key})
    return Response(status=403, data={'error': 'User credential error!'})


def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.activation_code = generate_verification_code()
            user.is_active_user = False
            user.save()

            return render(request, 'registration/success.html', {'user': user})
    else:
        form = RegistrationForm()

    return render(request, 'registration/register.html', {'form': form})


def generate_verification_code():
    return str(random.randint(100000, 999999))
