
from rest_framework import serializers
from .models import PantryItem, PantryOrder

class EmailSerializer(serializers.Serializer):
    subject = serializers.CharField()
    message = serializers.CharField()
    recipient = serializers.ListField(child=serializers.EmailField())


class PantryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PantryItem
        fields = '__all__'

class PantryOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PantryOrder
        fields = '__all__'
