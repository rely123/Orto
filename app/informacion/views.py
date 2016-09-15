from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView,UpdateView
from django.http import HttpResponse
from django.views.generic import ListView

from app.informacion.models import estado_general,datos_generales,fichas
from app.informacion.forms import EstadoGeneralForm,EstadoGeneralForm_consultar,DatosGeneralesForm

class EstadoGeneralList(ListView):
	model = estado_general
	template_name = 'informacion/list.html'



def EstadoGeneral_edit(request,codigo,num):
	str(codigo)
	ids = fichas.objects.get(cod_expediente=codigo, numero=num)
	if ids:
		estado = estado_general.objects.get(fichas_id=ids.id)
		if request.method == 'GET':
			form = EstadoGeneralForm(instance=estado)
		else: 
			form = EstadoGeneralForm(request.POST, instance=estado)
			if form.is_valid():
				form.save()
			return redirect('informacion:estado_general_listar')
		return render(request,'informacion/form_estadoGeneral.html',{'form':form})
	return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha")




def EstadoGeneral_consultar(request,codigo,num):
	str(codigo)
	ids = fichas.objects.get(cod_expediente=codigo, numero=num)
	if ids:
		estado = estado_general.objects.get(fichas_id=ids.id)
		if request.method == 'GET':
			form = EstadoGeneralForm_consultar(instance=estado)
		else: 
			form = EstadoGeneralForm_consultar(request.POST, instance=estado)
			if form.is_valid():
				form.save()
			return redirect('informacion:estado_general_listar')
		return render(request,'informacion/form_estadoGeneral.html',{'form':form})
	return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha")

DatosGeneralesForm


def EstadoGeneral_crear(request,codigo,num):
	str(codigo)
	try:
		ids = fichas.objects.get(cod_expediente=codigo, numero=num)
		if ids:
			if request.method == 'POST':

					form = EstadoGeneralForm(request.POST,initial={'fichas':ids.id})
					if form.is_valid():
					 	form.save()

					return redirect('informacion:estado_general_listar')
				
			else:
				form = EstadoGeneralForm(initial={'fichas':ids.id})

			return render(request, 'informacion/form_estadoGeneral.html', {'form':form})
	except Exception, e:
		return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha")

def DatosGeneral_crear(request):
		if request.method == 'POST':
				form = DatosGeneralesForm(request.POST)
				if form.is_valid():
				 	form.save()
				return redirect('informacion:datos_generales_listar')
				
		else:
				form = DatosGeneralesForm()

		return render(request, 'informacion/form_datosGenerales.html', {'form':form})
