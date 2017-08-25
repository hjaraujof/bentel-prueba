from django.db import models
from django_countries.fields import CountryField

class Cocinero(models.Model):
    nombre = models.CharField(max_length=40, blank=False)
    apellido = models.CharField(max_length=60,blank=True)
    email = models.EmailField(max_length=40, blank=False, primary_key=True)

class Alumno(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=40, blank=False)
    apellido = models.CharField(max_length=60,blank=True)
    codigoPostal = models.CharField(max_length=10, blank=False)
    codigoPais = CountryField(blank_label='(seleccione su pais)')
    class Meta:
        index_together = [
            ["nombre", "codigoPostal", "codigoPais"],
        ]

class Curso(models.Model):
    nombre = models.CharField(max_length=60, blank=False, primary_key=True)
    descripcion = models.TextField(blank=False)
    fechaInicio = models.DateTimeField(auto_now=False)
    fechaFin = models.DateTimeField(auto_now=False)
    cocinero = models.ForeignKey(Cocinero, related_name='cursos', on_delete=models.DO_NOTHING)
    inscritos = models.ForeignKey(Alumno, related_name='cursos', on_delete=models.DO_NOTHING,null=True)