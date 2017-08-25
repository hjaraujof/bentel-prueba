from django.conf.urls import url, include
from rest_framework import routers
from project.api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'cocineros', views.CocineroViewSet)
router.register(r'alumnos', views.AlumnoViewSet)
router.register(r'cursos', views.CursoViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]