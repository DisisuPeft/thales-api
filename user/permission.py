from rest_framework.permissions import BasePermission, SAFE_METHODS

class EsAutorORolPermitido(BasePermission):
    def __init__(self, roles_permitidos=None):
        self.roles_permitidos = roles_permitidos or ["Administrador"]
        
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        user = request.user
        is_autor = obj.usuario_id == user.id
        has_role = user.roleID.filter(name__in=self.roles_permitidos).exists()
        return is_autor or has_role
    
def EsAutorORolPermitidoConRoles(roles_permitidos):
    class CustomPermission(EsAutorORolPermitido):
        def __init__(self):
            super().__init__(roles_permitidos)
    return CustomPermission

"""
Ahora los permisos nativos de django

"""
class HasRole(BasePermission):
    allowed_roles = []

    def __init__(self, allowed_roles=None):
        self.allowed_roles = allowed_roles or []

    def has_access(self, request, view):
        user = request.user
        if not user or not user.is_authenticated:
            raise PermissionDenied("El usuario no está autenticado.")
        
        if not user.roles.filter(name__in=self.allowed_roles).exists():
            raise PermissionDenied(f"El usuario no tiene los roles requeridos")
        
        return True

# Método de fábrica para definir roles dinámicos
def HasRoleWithRoles(allowed_roles):
    class CustomHasRole(HasRole):
        def __init__(self):
            super().__init__(allowed_roles=allowed_roles)

    return CustomHasRole