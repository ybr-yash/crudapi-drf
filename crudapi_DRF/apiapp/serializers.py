from django.db.models import fields
from rest_framework import serializers
from .models import *

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'