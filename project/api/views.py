from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.forms import model_to_dict
from project.api.models import Cocinero, Alumno, Curso
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from project.api.serializers import UserSerializer, GroupSerializer, CocineroSerializer, CursoSerializer, AlumnoSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAdminUser,)

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (permissions.IsAdminUser,)

class CocineroViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows cocineros to be viewed or edited.
    """
    queryset = Cocinero.objects.all()
    serializer_class = CocineroSerializer
    permission_classes = (permissions.IsAdminUser,)

class AlumnoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows alumnos to be viewed or edited.
    """
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer
    permission_classes = (permissions.IsAdminUser,)

class CursoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows cursos to be viewed or edited.
    """
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    permission_classes = (permissions.IsAdminUser,)

@api_view(['GET', 'POST'])
def curso_alumno_list(request, name,format=None):
    alumnos = Alumno.objects.all()
    cursos = Curso.objects.all()
    try:
        curso = cursos.filter(nombre=name)[0]
        curso_dict = model_to_dict(curso,fields = ['nombre', 'descripcion','fechaInicio','fechaFin','cocinero'])
        print(curso)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        alumnos = Alumno.objects.filter(cursos=curso)
        serializer = AlumnoSerializer(alumnos, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        alumno = alumnos.filter(nombre=request.data["nombre"],
                                codigoPostal=request.data["codigoPostal"],
                                codigoPais=request.data["codigoPais"])
        if alumno.exists():
            alumno[0].cursos.add(curso)
            return Response(AlumnoSerializer(alumno[0], many=False).data, status=status.HTTP_201_CREATED)
        else:
            request.data["cursos"] = [curso]
            serializer = AlumnoSerializer(data=request.data)
            print(request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)