from django.contrib.auth.models import User
from rest_framework import serializers

from drinks.models import Drink


class DrinkSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Drink
        fields = ['id', 'name', 'description', 'owner']


class DrinkResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = ['name', 'description']


class UserSerializer(serializers.ModelSerializer):
    drinks = DrinkResponseSerializer(many=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'drinks']
