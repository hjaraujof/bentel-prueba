from django.contrib.auth.models import User, Group
from project.api.models import Cocinero, Alumno, Curso
from rest_framework import serializers

class PrimaryKeyRelatedField(serializers.PrimaryKeyRelatedField):
    def to_internal_value(self, data):
        return self.get_queryset().get(pk=data)

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
class CocineroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cocinero
        fields = ('nombre', 'apellido', 'email')
class CursoSerializer(serializers.HyperlinkedModelSerializer):
    cocinero = PrimaryKeyRelatedField(many=False, queryset=Cocinero.objects.all())
    class Meta:
        model = Curso
        fields = ('nombre', 'descripcion','fechaInicio','fechaFin','cocinero')
        depth = 1
class AlumnoSerializer(serializers.HyperlinkedModelSerializer):
    cursos = CursoSerializer(many=True,read_only=True)
    class Meta:
        model = Alumno
        fields = ('nombre', 'apellido','codigoPostal','codigoPais','cursos')