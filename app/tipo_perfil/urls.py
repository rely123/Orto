from django.conf.urls import url, include
from app.tipo_perfil.views import tipo_perfil, tipo_perfil_view, tipo_perfil_edit

urlpatterns = [
    url(r'^$', tipo_perfil, name='tipo_perfil'),
    url(r'^nuevo$', tipo_perfil_view, name='tipo_perfil_crear'),
    url(r'^edit/(?P<id_tipo_perfil>\d+)/$', tipo_perfil_edit, name='tipo_perfil_edit'),
]