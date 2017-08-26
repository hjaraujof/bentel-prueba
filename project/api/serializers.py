from django.contrib.auth.models import User, Group
from project.api.models import Cocinero, Alumno, Curso
from rest_framework import serializers, generics

class CocineroSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Cocinero
        fields = ('first_name', 'last_name', 'email')

class CursoSerializer(generics.GenericAPIView):

    class Meta:
        model = Curso
        fields = ('nombre', 'descripcion','fechaInicio','fechaFin')

    def get_serializer_context(self):
        """
        Extra context provided to the serializer class.
        """
        return { 'request': self.request, 'format': self.format_kwarg, 'view': self }

    def get_serializer(self, *args, **kwargs):
        """
        Return the serializer instance that should be used for validating and
        deserializing input, and for serializing output.
        """
        serializer_class = self.get_serializer_class()
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)

    def get_queryset(self):
        return Curso.objects.all().filter(cocinero=self.context['request'].user.email)

    def perform_create(self, serializer):
        serializer.save(cocinero=self.context['request'].user.email)

class AlumnoSerializer(serializers.HyperlinkedModelSerializer):

    cursos = CursoSerializer(many=True,read_only=True)

    class Meta:
        model = Alumno
        fields = ('nombre', 'apellido','codigoPostal','codigoPais','cursos')