# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-20 02:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FacialFrontal',
            fields=[
                ('id_frontal_facial', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('frontal_facial', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PerfilTotal',
            fields=[
                ('id_tipoPerfiltotal', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('tipoPerfiltotal', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PTercioInferioir',
            fields=[
                ('id_perfilTercio_inferior', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('perfilTercio_inferior', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Sonrisa',
            fields=[
                ('id_tipoSonrisa', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('tipoSonrisa', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TipoPerfil',
            fields=[
                ('id_tipo_perfil', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('tipoNariz', models.CharField(max_length=25)),
                ('angulo_Naso_labial', models.IntegerField()),
                ('tercio_superior', models.IntegerField()),
                ('tercio_medio', models.IntegerField()),
                ('tercio_inferior', models.IntegerField()),
                ('tamanoSonrisa', models.IntegerField()),
                ('grosorLabios', models.IntegerField()),
                ('tamanoLabios', models.IntegerField()),
                ('tipo_competenciaLabial', models.CharField(max_length=50)),
                ('id_frontal_facial', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tipo_perfil.FacialFrontal')),
                ('id_perfilTercio_inferior', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tipo_perfil.PTercioInferioir')),
                ('id_tipoPerfiltotal', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tipo_perfil.PerfilTotal')),
                ('id_tipoSonrisa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tipo_perfil.Sonrisa')),
            ],
        ),
    ]
