from django.db import models
from common.models import BaseCRM, OwnerBaseModel


class Campania(BaseCRM, OwnerBaseModel):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    programa = models.ForeignKey('control_escolar.ProgramaEducativo', on_delete=models.CASCADE, related_name='campanias', null=True, blank=True)
    costo_asignado = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)