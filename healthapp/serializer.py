# serializers transform complex django models into json format

from rest_framework import serializers
from .models import Data

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        # fields to integrate in API and data model to serialize
        fields =('name', 'description')
        