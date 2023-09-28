from django.contrib.auth.models import User

from .models import Drink
from .serializers import DrinkSerializer, UserSerializer

from rest_framework import generics


class DrinkList(generics.ListCreateAPIView):
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class DrinkDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetails(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
