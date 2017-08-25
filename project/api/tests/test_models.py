from django.test import TestCase
from ..models import Cocinero, Alumno, Curso

class CocineroTest(TestCase):
    """This class defines the test suite for the Cocinero model."""
    def setUp(self):
        """Define the test client and other test variables."""
        self.Cocinero_email = "cocinero_prueba@prueba.com"
        self.Cocinero = Cocinero(email=self.Cocinero_email)
        pass

    def test_model_can_create_a_Cocinero(self):
        """Test the Cocinero model can create a Cocinero."""
        old_count = Cocinero.objects.count()
        self.Cocinero.save()
        new_count = Cocinero.objects.count()
        self.assertNotEqual(old_count, new_count)

class AlumnoTest(TestCase):
    """This class defines the test suite for the Alumno model."""
    def setUp(self):
        """Define the test client and other test variables."""
        self.Alumno_nombre = "Pedro"
        self.Alumno_apellido = "Perez"
        self.Alumno_codigoPostal = "123456"
        self.Alumno_codigoPais = "MX"
        self.Alumno_email = "Alumno_prueba@prueba.com"
        self.Alumno = Alumno(nombre=self.Alumno_nombre,
                             apellido=self.Alumno_apellido,
                             codigoPostal=self.Alumno_codigoPostal,
                             codigoPais=self.Alumno_codigoPais,
                             email=self.Alumno_email)
        pass

    def test_model_can_create_a_Alumno(self):
        """Test the Alumno model can create a Alumno."""
        old_count = Alumno.objects.count()
        self.Alumno.save()
        new_count = Alumno.objects.count()
        self.assertNotEqual(old_count, new_count)

class CursoTest(TestCase):
    """This class defines the test suite for the Curso model."""
    def setUp(self):
        """Define the test client and other test variables."""
        self.Curso_nombreUnico = "Pedro"
        self.Curso_descripcion = "Perez"
        self.Curso_fechaInicio = "24/08/2017"
        self.Curso_fechaFin = "24/09/2017"
        self.Curso_cocinero = "cocinero_prueba@prueba.com"
        self.Curso = Curso(nombreUnico=self.Curso_nombreUnico,
                           descripcion=self.Curso_descripcion,
                           fechaInicio=self.Curso_fechaInicio,
                           fechaFin=self.Curso_fechaFin,
                           cocinero=self.Curso_cocinero)
        pass

    def test_model_can_create_a_Curso(self):
        """Test the Curso model can create a Curso."""
        old_count = Curso.objects.count()
        self.Curso.save()
        new_count = Curso.objects.count()
        self.assertNotEqual(old_count, new_count)