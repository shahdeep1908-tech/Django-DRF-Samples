from rest_framework import generics

from .models import BarTender
from .permissions import AuthenticateBarTender
from .serializers import BarTenderSerializer


class BartenderList(generics.ListCreateAPIView):
    queryset = BarTender.objects.all()
    serializer_class = BarTenderSerializer
    permission_classes = [AuthenticateBarTender]


class BartenderDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = BarTender.objects.all()
    serializer_class = BarTenderSerializer
    permission_classes = [AuthenticateBarTender]
