from django.contrib.auth.models import User
from rest_framework.response import Response

from .models import Drink
from .permissions import AuthenticateCreateAndAllowList, AuthenticateDrinkDetails, OnlyAdminAccessUserList, \
    OnlyParticularAdminAccessUserDetail
from .serializers import DrinkSerializer, UserSerializer

from rest_framework import generics, status


class DrinkList(generics.ListCreateAPIView):
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer
    permission_classes = [AuthenticateCreateAndAllowList]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class DrinkDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer
    permission_classes = [AuthenticateDrinkDetails]

    def put(self, request, *args, **kwargs):
        drink_owner_id = self.get_object().owner.id
        if request.user.id == drink_owner_id:
            return self.update(request, *args, **kwargs)
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [OnlyAdminAccessUserList]


class UserDetails(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [OnlyParticularAdminAccessUserDetail]
