from __future__ import unicode_literals
from django.db import models
#from app.informacion.models import datos_generales

# Create your models here.

class FacialFrontal(models.Model):
	id_frontal_facial = models.CharField(max_length=10, primary_key=True)
	frontal_facial = models.CharField(max_length=50)

	#def __unicode__(self):
    #     return '{}'.format(self.frontal_facial)


class PerfilTotal(models.Model):
	id_tipoPerfiltotal = models.CharField(max_length=10, primary_key=True)
	tipoPerfiltotal = models.CharField(max_length=50)

	#def __unicode__(self):
    #    return '{}'.format(self.tipoPerfiltotal)


class PTercioInferioir(models.Model):
	id_perfilTercio_inferior = models.CharField(max_length=10, primary_key=True)
	perfilTercio_inferior = models.CharField(max_length=50)

	#def __unicode__(self):
    #    return '{}'.format(self.perfilTercio_inferior)


class Sonrisa(models.Model):
	id_tipoSonrisa = models.CharField(max_length=10, primary_key=True)
	tipoSonrisa = models.CharField(max_length=50)

	#def __unicode__(self):
    #    return '{}'.format(self.tipoSonrisa)


class TipoPerfil(models.Model):

	id_tipo_perfil = models.CharField(max_length=10, primary_key=True)	
	#cod_expediente = models.ForeignKey(FacialFrontal, null=True, blank=True, on_delete=models.CASCADE)

	id_frontal_facial = models.ForeignKey(FacialFrontal, null=True, blank=True, on_delete=models.CASCADE)
	id_tipoPerfiltotal = models.ForeignKey(PerfilTotal, null=True, blank=True, on_delete=models.CASCADE)
	id_perfilTercio_inferior = models.ForeignKey(PTercioInferioir, null=True, blank=True, on_delete=models.CASCADE)
	id_tipoSonrisa = models.ForeignKey(Sonrisa, null=True, blank=True, on_delete=models.CASCADE)

	tipoNariz = models.CharField(max_length=25)
	angulo_Naso_labial = models.IntegerField()
	tercio_superior = models.IntegerField()
	tercio_medio = models.IntegerField()
	tercio_inferior = models.IntegerField()
	tamanoSonrisa = models.IntegerField()
	grosorLabios= models.IntegerField()
	tamanoLabios = models.IntegerField()
	tipo_competenciaLabial = models.CharField(max_length=50)


	#def __unicode__(self):
    #    return '{}'.format(self.id_tipo_perfil)

		

