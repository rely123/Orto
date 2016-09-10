from django.contrib import admin
# -*- coding: utf-8 -*-

from app.informacion.models import datos_generales,estado_general,catalogo_enfermedades
from app.informacion.models import fichas

# Register your models here.

admin.site.register(datos_generales)
admin.site.register(fichas)
admin.site.register(estado_general)
admin.site.register(catalogo_enfermedades)
