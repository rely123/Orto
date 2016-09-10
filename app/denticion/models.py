from __future__ import unicode_literals

from django.db import models
from app.informacion.models import datos_generales
from app.informacion.models import fichas

# Create your models here.

class linea_media_facial(models.Model):
	datos_generales = models.ForeignKey(datos_generales, null=False, blank=False, on_delete=models.CASCADE)
	fichas = models.OneToOneField(fichas, null=False, blank=False, on_delete=models.CASCADE)
	mx = models.IntegerField()
	mx_desviacion = models.IntegerField()
	md = models.IntegerField()
	md_desviacion = models.IntegerField()

	def __str__(self):
		return '{}'.format(self.fichas)

class sobremordidas(models.Model):
	datos_generales = models.ForeignKey(datos_generales, null=False, blank=False, on_delete=models.CASCADE)
	fichas = models.OneToOneField(fichas, null=False, blank=False, on_delete=models.CASCADE)
	horizontal = models.IntegerField()
	vertical = models.IntegerField()

	def __str__(self):
		return '{}'.format(self.fichas)

class registro_mordidas(models.Model):
	datos_generales = models.ForeignKey(datos_generales, null=False, blank=False, on_delete=models.CASCADE)
	fichas = models.OneToOneField(fichas, null=False, blank=False, on_delete=models.CASCADE)
	cuad_superior = models.IntegerField()
	pieza_superior = models.IntegerField()
	cuad_inferior = models.IntegerField()
	pieza_inferior = models.IntegerField()

	def __str__(self):
		return '{}'.format(self.fichas)