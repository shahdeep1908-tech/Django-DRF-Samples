from django.contrib.auth.models import User
from rest_framework import serializers

from drinks.models import Drink
from bartender.serializers import BarTenderDetailsSerializer


class DrinkSerializer(serializers.ModelSerializer):
    bartenders = BarTenderDetailsSerializer(many=True, read_only=True)

    class Meta:
        model = Drink
        fields = ['id', 'name', 'description', 'bartenders']


class DrinkResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = ['name', 'description']


class UserSerializer(serializers.ModelSerializer):
    drinks = DrinkResponseSerializer(many=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'drinks']
