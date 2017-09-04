from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers
from project.api import views

router = routers.DefaultRouter()
router.register(r'alumnos', views.AlumnoViewSet)
router.register(r'cursos', views.CursoViewSet)
urlpatterns = [
    url(r'^api/', include(router.urls)),    
    url(r'^api/cursos/(?P<name>[a-zA-Z0-9-]+)/curso_alumno/$', views.curso_alumno_list, name='alumnos_list'),
]