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
class AlumnoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Alumno
        fields = ('nombre', 'apellido','codigoPostal','codigoPais')
class CursoSerializer(serializers.HyperlinkedModelSerializer):
    cocinero = PrimaryKeyRelatedField(many=False, queryset=Cocinero.objects.all())
    inscritos = AlumnoSerializer(many=True,allow_null=True)
    class Meta:
        model = Curso
        fields = ('nombre', 'descripcion','fechaInicio','fechaFin','cocinero','inscritos')
        depth = 1
    def create(self, validated_data):
        inscritos_data = validated_data.pop('inscritos')
        curso = Curso.objects.create(**validated_data)
        for inscrito_data in inscritos_data:
            print(inscrito_data)
            Alumno.objects.create(cursos=curso, **inscrito_data)        
        return curso