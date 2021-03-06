from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView,UpdateView
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.base import RedirectView
from django.http import HttpResponseRedirect	
from collections import OrderedDict

from app.informacion.models import *
from app.informacion.forms import *


class DatosGeneralesList(ListView):
	model = datos_generales
	template_name = 'informacion/list_datosgenerales.html'

codi="0000-00"
def DatosGeneral_crear(request):
	
		if request.method == 'POST':
				form = DatosGeneralesForm(request.POST)
				if form.is_valid():
					global codi
					codi = request.POST.get('cod_expediente')
				 	form.save()
				return HttpResponseRedirect('/informacion/fichas/nuevo/%s/' %codi) 
		else:
				form = DatosGeneralesForm()

		return render(request, 'informacion/form_datosGenerales.html', {'form':form})

def DatosGenerales_consultar(request,codi):
	str(codi)
	try:
		ids = datos_generales.objects.get(cod_expediente=codi)
		if ids:
			datos = datos_generales.objects.get(cod_expediente=codi)
			if request.method == 'GET':
				form = DatosGeneralesForm_consultar(instance=datos)
			else: 
				form = DatosGeneralesForm_consultar(request.POST, instance=datos)
				if form.is_valid():
					form.save()
				return redirect('informacion:datos_generales_listar')
			return render(request,'informacion/form_datosGenerales.html',{'form':form})
		return HttpResponse("No se encontro el Codigo de Expediente")
	except Exception, e:
		return HttpResponse("No se encontro el Codigo de Expediente")

def DatosGenerales_edit(request,codi):
	str(codi)
	try:
		ids = datos_generales.objects.get(cod_expediente=codi)
		if ids:
			datos = datos_generales.objects.get(cod_expediente=codi)
			if request.method == 'GET':
				form = DatosGeneralesForm(instance=datos)
			else: 
				form = DatosGeneralesForm(request.POST, instance=datos)
				if form.is_valid():
					co = request.POST.get('cod_expediente')
					form.save()
				#return redirect('informacion:datos_generales_listar')
				return HttpResponseRedirect('/informacion/fichas/nuevo/%s/' %co)
			return render(request,'informacion/form_datosGenerales.html',{'form':form})
		return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha")
	except Exception, e:
		return HttpResponse("No se encontro el Codigo de Expediente")




##################################################################################################

class FichasList(ListView):
	model = fichas
	template_name = 'informacion/list_fichas.html'


num=1
def Fichas_crear(request,codi):
	str(codi)
	ids = datos_generales.objects.get(cod_expediente=codi)

	d=OrderedDict()
 	fi=list(fichas.objects.filter(cod_expediente=codi))
 	if fi:
	 	ultimo = fi[-1]
	 	numer=ultimo.numero+1
	else:
	 	numer=1

	if ids:
		if request.method == 'POST':
				form = FichasForm(request.POST)
				if form.is_valid():
					global num
					num = request.POST.get('numero')
				 	form.save()
				
				return HttpResponseRedirect('/informacion/estado_general/nuevo/%s/%s/' %(codi,num))
		else:
			form = FichasForm(initial={'cod_expediente':codi,'numero':numer})

	return render(request, 'informacion/form_fichas.html', {'form':form, 'numer':numer})



##################################################################################################
class EstadoGeneralList(ListView):
	model = estado_general
	template_name = 'informacion/list_estadogeneral.html'

def EstadoGeneral_crear(request,codi,num):
	str(codi)
	try:
		ids = fichas.objects.get(cod_expediente=codi, numero=num)
		if ids:
			if request.method == 'POST':

					form = EstadoGeneralForm(request.POST,initial={'fichas':ids.id})
					if form.is_valid():
					 	form.save()

					return redirect('informacion:estado_general_listar')
				
			else:
				form = EstadoGeneralForm(initial={'fichas':ids.id})

		return render(request, 'informacion/form_estadoGeneral.html', {'form':form,'codi': codi})
	except Exception, e:
		return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha")

def EstadoGeneral_consultar(request,codi,num):
	str(codi)
	try:
		ids = fichas.objects.get(cod_expediente=codi, numero=num)
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
		return HttpResponsze("No se encontro el Codigo de Expediente y el numero de la ficha")
	except Exception, e:
		return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha")

def EstadoGeneral_edit(request,codi,num):
	str(codi)
	try:
		ids = fichas.objects.get(cod_expediente=codi, numero=num)
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
	except Exception, e:
		return HttpResponse("No se encontro el Codigo de Expediente y el numero de la ficha")












################################################################################################


