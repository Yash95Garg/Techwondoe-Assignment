from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email')


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ('CompanyID', 'CompanyName', 'CompanyCEO', 'CompanyAddress', 'InceptionDate')

class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = ('TeamID', 'CompanyID', 'TeamLead')
