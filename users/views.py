from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token

from django.contrib.auth.models import User
from django.contrib.auth import authenticate


# Create your views here.
@api_view(['POST'])
# @permission_classes([AllowAny])
def sign_in(request):
    if request.method == 'POST':
        data = request.data

        user = authenticate(username=request.data['id'], password=request.data['password'])

        if user:
            # get_or_create returns tuple (token: token, is_created: bool)
            token = Token.objects.get_or_create(user=user)[0]

            return Response({"Token": token.key})
        else:
            return Response(status=401)


@api_view(['POST'])
def sign_up(request):
    if request.method == 'POST':
        data = request.data
        user = User.objects.create_user(username=data['id'], password=data['password'])

        user.save()

        token = Token.objects.create(user=user)
        return Response({"Token": token.key})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def sign_out(request):
    if request.method == 'POST':
        request.user.auth_token.delete()

        return Response(status=204)
