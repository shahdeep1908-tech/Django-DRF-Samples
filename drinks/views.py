from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Drink
from .serializers import DrinkSerializer

from rest_framework.decorators import api_view


class DrinkList(APIView):
    def get(self, request, format=None):
        drinks = Drink.objects.all()
        serializer = DrinkSerializer(drinks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = DrinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class DrinkDetails(APIView):
    @staticmethod
    def get_object(pk):
        try:
            return Drink.objects.get(pk=pk)
        except Drink.DoesNotExist as e:
            raise Http404 from e

    def get(self, request, id, format=None):
        drink = self.get_object(id)
        serializer = DrinkSerializer(drink)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id, format=None):
        drink = self.get_object(id)
        serializer = DrinkSerializer(drink, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        drink = self.get_object(id)
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
