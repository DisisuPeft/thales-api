from user.models import UserCustomize as User
from rest_framework import serializers
from django.db import transaction
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate
from rest_framework import exceptions

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = 'email'

    def validate(self, attrs):
        credentials = {
            'email': attrs.get('email'),
            'password': attrs.get('password')
        }
        user = authenticate(**credentials)
        if user: 
            if not user.is_active:
                raise exceptions.AuthenticationFailed('User is deactivated')


class MeSerializer(serializers.ModelSerializer):
    # roles = serializers.SerializerMethodField()
    # permissions = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = ("uuid","email")
        
    # def get_roles(self, obj):
    #     return list(obj.groups.values_list("name", flat=True))

    # def get_permissions(self, obj):
    #     return sorted(list(obj.get_all_permissions()))
        



