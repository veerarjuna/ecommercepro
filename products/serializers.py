from rest_framework import serializers
from .models import Stores


class StoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stores
        fields = '__all__'