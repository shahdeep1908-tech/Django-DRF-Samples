from django.contrib.auth.models import User
from rest_framework.response import Response

from .models import Drink
from .permissions import AuthenticateCreateAndAllowList, AuthenticateDrinkDetails, OnlyAdminAccessUserList, \
    OnlyParticularAdminAccessUserDetail
from .serializers import DrinkSerializer, UserSerializer

from rest_framework import generics, status


class DrinkList(generics.ListCreateAPIView):
    serializer_class = DrinkSerializer
    permission_classes = [AuthenticateCreateAndAllowList]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Drink.objects.filter(owner=self.request.user)
        return Drink.objects.none()

    def create(self, request, *args, **kwargs):
        data = request.data
        many = isinstance(data, list)
        serializer = self.get_serializer(data=data, many=many)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status.HTTP_201_CREATED)

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
