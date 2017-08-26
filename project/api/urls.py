from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers
from project.api import views

router = routers.DefaultRouter()
#router.register(r'users', views.UserViewSet)
#router.register(r'groups', views.GroupViewSet)
router.register(r'cocineros', views.CocineroViewSet)
router.register(r'alumnos', views.AlumnoViewSet)
router.register(r'cursos', views.CursoViewSet)
#router.register(r'cursos/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/alumnos_list/$', views.curso_alumno_list, base_name='topic_content_list')
urlpatterns = [
    url(r'^api/', include(router.urls)),    
    url(r'^api/cursos/(?P<name>[a-zA-Z0-9-]+)/curso_alumno/$', views.curso_alumno_list, name='alumnos_list'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]