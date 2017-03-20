from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from django.contrib.auth import get_user_model

from SiO.member.models import Member, Association
from SiO.CoAdmin.models import Administrator
from django.core import serializers
from django.contrib.auth.decorators import login_required

from SiO.CoAdmin.serializers import AdministratorSerializer
from SiO.member.serializers import MemberSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework import generics
from rest_framework.authentication import BasicAuthentication
# from rest_framework_jwt.authentication import JSONWebTokenAuthentication


User = get_user_model()


# @login_required
class ChartView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'chart/ChartView.html', {})


# def get_data(request, *args, **kwargs):
#     data = {
#         "Sales": 100,
#         "Customers": 10,
#     }
#     return JsonResponse(data)

# @login_required
# class ChartData(generics.ListAPIView):
class ChartData(APIView):

    # serializer_class = AdministratorSerializer, MemberSerializer

    # authentication_classes = ([])
    # # authentication_classes = (authentication.TokenAuthentication,)
    # permission_classes = ([permissions.IsAdminUser])

    # @login_required
    def get(self, request, format=None):
    # def get_queryset(self):
        # usernames = [user.username for user in User.objects.all()]
        # qs_count = User.objects.all().count()
        # if Administrator.objects.filter(association=self.request.user.association):
        qs_count = Administrator.objects.filter(association=self.request.user.association).count()
        # qs_count1 = Member.objects.all().count()
        qs_count1 = Member.objects.filter(association=self.request.user.association).count()
        # qs_count2 = Association.objects.all().count()
        # qs_count2 = Association.objects.filter(association=self.request.user.association).count()
        labels = ["Board", "Members"]
        default_items = [qs_count, qs_count1]
        data = {
            "labels": labels,
            "default": default_items,
        }
        return Response(data)




