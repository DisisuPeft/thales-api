from user.models import UserCustomize as User
from user.models import Role
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
    modulos_accesibles = serializers.SerializerMethodField()
    # pestanias_accesibles = serializers.SerializerMethodField()
    nombre_completo = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ("uuid","email", 'nombre_completo', 'modulos_accesibles')
        
    def get_nombre_completo(self, obj):
        return f"{obj.nombre} {obj.apellido_paterno} {obj.apellido_materno}" if obj.nombre and obj.apellido_paterno and obj.apellido_materno else ""
        
    def get_modulos_accesibles(self, obj):
        from sistema.serializers import ModulosSerializer
        
        data = obj.modulos_accesibles()

        return ModulosSerializer(data, many=True).data

    # def get_pestanias_accesibles(self, obj):
    #     from sistema.serializers import PestianiaSerializer
        
    #     data = obj.pestanias_accesibles()

    #     return PestianiaSerializer(data, many=True).data



class UserSerializer(serializers.ModelSerializer):
    genero_name = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ("uuid", "nombre", "apellido_paterno", "apellido_materno", "genero",  "genero_name", "edad", "fecha_nacimiento", "telefono", "email", "status")

    def get_genero_name(self, obj):
        return obj.genero.nombre if obj.genero else None
    
class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ("uuid", "nombre")