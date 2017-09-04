from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from .managers import CocineroManager
from django.conf import settings

class Cocinero(AbstractBaseUser, PermissionsMixin):
    
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    is_staff = models.BooleanField()
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CocineroManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)

class Curso(models.Model):

    nombre = models.CharField(max_length=60, blank=False, primary_key=True)
    descripcion = models.TextField(blank=False)
    fechaInicio = models.DateTimeField(auto_now=False)
    fechaFin = models.DateTimeField(auto_now=False)
    cocinero = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='cursos', on_delete=models.DO_NOTHING,null=True)    

class Alumno(models.Model):

    nombre = models.CharField(max_length=40, blank=False)
    apellido = models.CharField(max_length=60,blank=True)
    codigoPostal = models.CharField(max_length=10, blank=False)
    codigoPais = CountryField(blank_label='(seleccione su pais)')
    cursos = models.ManyToManyField(Curso)

    class Meta:

        index_together = ["nombre", "codigoPostal", "codigoPais"]
        unique_together = ("nombre", "codigoPostal", "codigoPais")