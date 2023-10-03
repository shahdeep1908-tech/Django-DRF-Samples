from rest_framework import serializers

from bartender.models import BarTender


class BarTenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = BarTender
        fields = ['id', 'name', 'experience_years', 'drinks']
        extra_kwargs = {'drinks': {'required': False}}


class BarTenderDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BarTender
        fields = ['name', 'experience_years']
