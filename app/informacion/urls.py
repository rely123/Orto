from django.conf.urls import url,include
from django.contrib import admin

from app.informacion.views import EstadoGeneral_crear,EstadoGeneralList,EstadoGeneral_edit,EstadoGeneral_consultar
from app.informacion.views import DatosGeneral_crear,DatosGeneralesList,DatosGenerales_consultar,DatosGenerales_edit

urlpatterns = [
	url(r'^estado_general/nuevo/(?P<codigo>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/(?P<num>\d+)/$', EstadoGeneral_crear, name='estado_general_crear'),
	url(r'^estado_general/listar', EstadoGeneralList.as_view(),name='estado_general_listar'),
	url(r'^estado_general/editar/(?P<codigo>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/(?P<num>\d+)/$', EstadoGeneral_edit,name='estado_general_editar'),
	url(r'^estado_general/consultar/(?P<codigo>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/(?P<num>\d+)/$', EstadoGeneral_consultar,name='estado_general_consultar'),

	url(r'^datos_generales/nuevo/$', DatosGeneral_crear, name='datos_generales_crear'),
	url(r'^datos_generales/listar', DatosGeneralesList.as_view(),name='datos_generales_listar'),
	url(r'^datos_generales/consultar/(?P<codigo>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/$', DatosGenerales_consultar,name='datos_generales_consultar'),
	url(r'^datos_generales/editar/(?P<codigo>[0-9]{4}(.).*?((?:[a-z][a-z0-9_]*)?))/$', DatosGenerales_edit,name='datos_generales_editar'),



]