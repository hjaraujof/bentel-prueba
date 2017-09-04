from django.contrib.auth.models import User, Group
from project.api.models import Cocinero, Alumno, Curso
from rest_framework import serializers

class CocineroSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Cocinero
        depth = 1
        fields = ('first_name', 'last_name', 'email')

class CursoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Curso
        depth = 1
        fields = ('nombre', 'descripcion','fechaInicio','fechaFin')    

class AlumnoSerializer(serializers.HyperlinkedModelSerializer):

    cursos = CursoSerializer(many=True,read_only=True)

    class Meta:
        model = Alumno
        depth = 1
        fields = ('nombre', 'apellido','codigoPostal','codigoPais','cursos')