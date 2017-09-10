from django.contrib import admin
from .models import Cocinero

class CocineroAdmin(admin.ModelAdmin):
    fields = ('first_name', 'last_name','email','password')

# Register your models here.
admin.site.register(Cocinero, CocineroAdmin)