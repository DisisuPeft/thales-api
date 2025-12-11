from django.db import models
from common.models import Base, OwnerBaseModel

class TipoPrograma(Base, OwnerBaseModel):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    
    
    
class ModalidadesPrograma(Base, OwnerBaseModel):
    name = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True, null=True)
    sincronia = models.CharField(max_length=200, blank=True, null=True) 


class ProgramaEducativo(Base):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, null=True)
    tipo = models.ForeignKey(TipoPrograma, on_delete=models.CASCADE, related_name="programas", blank=True, null=True)
    institucion = models.ForeignKey(InstitucionAcademica, on_delete=models.CASCADE, related_name="programas", blank=True, null=True)
    duracion_horas = models.IntegerField(blank=True, null=True)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_fin = models.DateField(blank=True, null=True)
    duracion_meses = models.IntegerField(null=True, blank=True)
    # ciclo = models.ForeignKey(Ciclos, on_delete=models.SET_NULL, related_name="programa_educativo", null=True, blank=True)
    periodo_imparticion = models.ForeignKey(Periodos, on_delete=models.SET_NULL, related_name="programa_educativo", null=True, blank=True)
    horario = models.CharField(max_length=200, blank=True, null=True)  # ej. Sábados y Domingos de 8 a 14 hrs
    costo_inscripcion = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    costo_mensualidad = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    costo_documentacion = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    # inscripcion = models.ManyToManyField(Estudiante, related_name="program", null=True, blank=True)
    activo = models.IntegerField()
    instructor = models.ManyToManyField("user.UserCustomize", related_name="programas", null=True, blank=True)
    modalidad = models.ForeignKey(ModalidadesPrograma, on_delete=models.CASCADE, related_name="programas", null=True, blank=True)
    imagen_url = models.CharField(max_length=255, null=True, blank=True)
    banner_url = models.CharField(max_length=255, null=True, blank=True)