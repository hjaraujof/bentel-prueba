from django.views import generic
from django.shortcuts import render
from django.forms import model_to_dict
from project.api.models import Cocinero, Alumno, Curso
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from project.api.serializers import CocineroSerializer, CursoSerializer, AlumnoSerializer

class CursoListView(generic.ListView):
    model = Curso
    context_object_name = "lista_curso"
    query_set = Curso.objects.all()
    template_name = 'templates/curso/list.html'

class AlumnoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows alumnos to be viewed or edited.
    """
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer
    permission_classes = (permissions.IsAuthenticated,)

class CursoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows cursos to be viewed or edited.
    """
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    permission_classes = (permissions.IsAuthenticated,)

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
        return Curso.objects.all().filter(cocinero=self.request.user)

    def perform_create(self, serializer):
        serializer.save(cocinero=serializer.context['request'].user)

@api_view(['GET', 'POST'])
def curso_alumno_list(request, name,format=None):
    """
    API endpoint that allows the following:
        -GET Method: Listing Cursos for a logged in Cocinero.
        -POST Method: Adding(and creating if needed) Alumnos to a Curso
    """
    alumnos = Alumno.objects.all()
    cursos = Curso.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    try:
        curso = cursos.filter(nombre=name)[0]
        curso_dict = model_to_dict(
            curso,
            fields = ['nombre', 'descripcion','fechaInicio','fechaFin','cocinero']
        )
        print(curso)

    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        alumnos = Alumno.objects.filter(cursos=curso)
        serializer = AlumnoSerializer(alumnos, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        alumno = alumnos.filter(
            nombre=request.data["nombre"],
            codigoPostal=request.data["codigoPostal"],
            codigoPais=request.data["codigoPais"]
        )
        if alumno.exists():
            alumno[0].cursos.add(curso)
            return Response(
                AlumnoSerializer(alumno[0], many=False).data, 
                status=status.HTTP_201_CREATED
            )
        else:
            request.data["cursos"] = [curso]
            serializer = AlumnoSerializer(data=request.data)
            print(request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)