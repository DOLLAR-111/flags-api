from rest_framework import serializers
from .models import Flags


class FlagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flags
        fields = '__all__'