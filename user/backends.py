from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import Permission


class RolePermissionBackend(ModelBackend):
    """
    Backend que modifica completamente group 
    y obtiene permisos exclusivamente de role
    
    """

    def get_user_permissions(self, user_obj, obj=None):
        
        if not user_obj.is_active or not user_obj.is_authenticated:
            return set()
        
        permisos = set()
        for role in user_obj.roles.all():
            for perm in role.permission.all():
                permisos.add(f"{perm.content_type.app_label}.{perm.codename}")
        return permisos
    
    def get_group_permissions(self, user_obj, obj=None):
        """
            Django siempre pregunta, asi que aca se anula

        """
        
        return set()

    def get_all_permissions(self, user_obj, obj=None):
        if not user_obj.is_active or not user_obj.is_authenticated:
            return set()
        return self.get_user_permissions(user_obj)

    def has_perm(self, user_obj, perm, obj=None):
        if not user_obj.is_active or not user_obj.is_authenticated:
            return False
        return perm in self.get_all_permissions(user_obj)