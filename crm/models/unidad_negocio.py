from django.db import models
from common.models import BaseCRM, OwnerBaseModel

class UnidadNegocio(BaseCRM, OwnerBaseModel):
    nombre = models.CharField(max_length=100)
    user = models.ForeignKey('user.UserCustomize', on_delete=models.CASCADE, related_name='%(class)s_user', null=True, blank=True)

class PreferenciaCRM(BaseCRM, OwnerBaseModel):
    user = models.ForeignKey('user.UserCustomize', on_delete=models.CASCADE, related_name='%(class)s_user', null=True, blank=True)
    agrupar = models.BooleanField(default=False)