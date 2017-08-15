from rest_framework.views import APIView
from rest_framework import viewsets
from game.serializers import *
from rest_framework.response import Response
from game.models import *
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.http import Http404

class CurrentUserView(APIView):

    def get(self, request):
        #print('CurrentUser: {}'.format(request.user))
        #from django.contrib.auth.models import User
        serializer = UserSerializer(request.user)
        #serializer = UserSerializer(User.objects.get(pk=1))
        return Response(serializer.data)

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class PlayerGameViewSet(viewsets.ViewSet):
    """
    API endpoint for player games
    """

    def list(self, request):
        print('START')
        print(self.request.user)
        print(self.request.user.id)
        queryset = Game.get_games_for_player(self.request.user)
        # from django.contrib.auth.models import User
        # queryset = Game.get_games_for_player(User.objects.get(pk=1))
        print('END')
        serializer = GameSerializer(
            queryset, many=True, context={'request': request})
        return Response(serializer.data)
