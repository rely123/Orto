from django.conf.urls import url,include
from django.contrib import admin

from app.informacion.views import EstadoGeneral_crear,EstadoGeneralList,EstadoGeneral_edit,EstadoGeneral_consultar

urlpatterns = [
	url(r'^nuevo/(?P<codigo>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/(?P<num>\d+)/$', EstadoGeneral_crear, name='estado_general_crear'),
	url(r'^listar', EstadoGeneralList.as_view(),name='estado_general_listar'),
	url(r'^editar/(?P<codigo>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/(?P<num>\d+)/$', EstadoGeneral_edit,name='estado_general_editar'),
	url(r'^consultar/(?P<codigo>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/(?P<num>\d+)/$', EstadoGeneral_consultar,name='estado_general_consultar'),


]