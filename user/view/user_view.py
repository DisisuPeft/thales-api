from rest_framework import status, viewsets
from user.permission import EsAutorORolPermitido, HasRoleWithRoles
from rest_framework.permissions import IsAuthenticated
from user.authenticate import CustomJWTAuthentication
from rest_framework.response import Response
from user.models import UserCustomize as User
from user.serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, HasRoleWithRoles(["Administrador"])]
    queryset = User.objects.all()
    authentication_classes = [CustomJWTAuthentication]
    serializer_class = UserSerializer



    def get_queryset(self):
        user = self.request.user
        qs = super().get_queryset()
        qs = qs.exclude(email=user.email)

        return qs


