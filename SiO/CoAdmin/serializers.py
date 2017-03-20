from rest_framework import serializers
from SiO.CoAdmin.models import Administrator


class AdministratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrator
        fields = ['id', 'user']


