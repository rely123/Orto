
from django.shortcuts import render, redirect
from django.http import HttpResponse

from app.tipo_perfil.forms import Tipo_perfilForm 
from app.tipo_perfil.models import TipoPerfil, FacialFrontal, PerfilTotal   
from app.tipo_perfil.models import PTercioInferioir, Sonrisa

# Create your views here.

def tipo_perfil(request):
	return render(request, 'tipo_perfil/tipo_perfil.html')


def tipo_perfil_view(request):
	if request.method == 'POST':
		form = Tipo_perfilForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('tipo_perfil:tipo_perfil')
	else: 
		form = Tipo_perfilForm()
	return render(request,'tipo_perfil/form_tipo_perfil.html', {'form':form})




def tipo_perfil_edit(request,codigo):
	str(codigo)
	ids = TipoPerfil.objects.get(id_tipo_perfil=codigo)
	if ids:
		datos = TipoPerfil.objects.get(id_tipo_perfil=codigo)
		if request.method == 'GET':
			form = Tipo_perfilForm(instance=datos)
		else: 
			form = Tipo_perfilForm(request.POST, instance=datos)
			if form.is_valid():
				#co = request.POST.get('id_tipo_perfil')
				form.save()
			return redirect('tipo_perfil:tipo_perfil_crear')
		return render(request, 'tipo_perfil/form_tipo_perfil.html',{'form':form})
	return HttpResponse("No se encontro el identificador del tipo de perfil")





