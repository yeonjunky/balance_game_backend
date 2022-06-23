from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
import rest_framework.authtoken.views

from django.contrib.auth.models import User


# Create your views here.
@api_view(['POST'])
def sign_in(request):
    if request.method == 'POST':
        data = request.data

    return None


@api_view(['POST'])
def sign_up(request):
    if request.method == 'POST':
        data = request.data
        user = User(username=data['id'], password=data['password'])

        user.save()

        token = Token.objects.create(user=user)
        return Response({"Token": token.key})
