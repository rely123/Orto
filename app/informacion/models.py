from __future__ import unicode_literals
from django.db import models
from app.informacion.choices import genero_choices



# Create your models here.

class datos_generales(models.Model):
    cod_expediente = models.CharField(max_length=10, primary_key=True)
    nombre_completo = models.CharField(max_length=100)
    edad = models.IntegerField()
    edad_registro = models.IntegerField()
    fecha_nac = models.DateField()
    telefono = models.CharField(max_length=8)
    genero = models.IntegerField(choices=genero_choices, default=1)
    direccion = models.CharField(max_length=200)
    nombre_resp = models.CharField(max_length=100)
    motivo_consulta = models.CharField(max_length=500)
    fechaRegistro = models.DateField() 
    #usuario_creador = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='usuario_creador',null=True)
    fecha_hora_creacion = models.DateTimeField()

    def __unicode__(self):
        return '{}'.format(self.cod_expediente)

class fichas(models.Model):
    cod_expediente = models.ForeignKey(datos_generales, null=False, blank=False, on_delete=models.CASCADE)
    numero = models.IntegerField()

    class Meta:
        unique_together = [("cod_expediente", "numero")]
        ordering = ['cod_expediente']


    def __unicode__(self):
        return 'Expediente: %s Fichas: %s' % (self.cod_expediente,self.numero)

class catalogo_enfermedades(models.Model):
    id_enfermedad = models.IntegerField(primary_key=True)
    nombre_enfermedad = models.CharField(max_length=30)

    def __unicode__(self):
        return  '{} {}'.format(self.id_enfermedad,self.nombre_enfermedad)


class estado_general(models.Model):
    fichas = models.OneToOneField(fichas, null=False, blank=False, on_delete=models.CASCADE)
    cambio_salud = models.BooleanField()
    detalle_enf_operacion = models.CharField(max_length=500, blank=True, null=True)
    detalle_medicamento = models.CharField(max_length=30, blank=True, null=True)
    detalle_otra_enfermedad = models.CharField(max_length=30,null=True,blank=True)
    otras_enfermedades = models.ManyToManyField(catalogo_enfermedades,null=True,blank=True)
    
    def __unicode__(self):
        return '{}'.format(self.fichas)

