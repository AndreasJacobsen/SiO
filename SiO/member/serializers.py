from rest_framework import serializers
from SiO.member.models import Member, Association


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['id']


class AssociationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Association
        fields = ['id']


