from django import forms
from app.informacion.models import estado_general,fichas,datos_generales
# -*- coding: utf-8 -*-

class EstadoGeneralForm(forms.ModelForm):
	class Meta:
		model = estado_general

		fields = [
			'fichas',
			'cambio_salud',
			'detalle_enf_operacion',
			'detalle_medicamento',
			'detalle_otra_enfermedad',
			'otras_enfermedades',
		]

		labels ={
			'fichas': 'Codigo Expediente y Numero de Ficha'	,
			'cambio_salud' : 'Cambio de Salud  ',
			'detalle_enf_operacion' : 'En que Consistio la enfermedad u operacion',
			'detalle_medicamento' : 'Medicamento Que ha tomado',
			'detalle_otra_enfermedad' : 'otras enfermedades',
			'otras_enfermedades': 'Tuvo alguna de estas enfermedades ',
		}
		widgets={
			'fichas':forms.HiddenInput(attrs={'class':'form-control'}),
			'cambio_salud':forms.CheckboxInput(attrs={}),
			'detalle_enf_operacion':forms.Textarea(attrs={'class':'form-control','disabled':True}),
			'detalle_medicamento':forms.TextInput(attrs={'class':'form-control','disabled':True}),
			'detalle_otra_enfermedad':forms.TextInput(attrs={'class':'form-control'}),
			'otras_enfermedades': forms.CheckboxSelectMultiple(),
		}


class EstadoGeneralForm_consultar(forms.ModelForm):
	class Meta:
		model = estado_general

		fields = [
			'fichas',
			'cambio_salud',
			'detalle_enf_operacion',
			'detalle_medicamento',
			'detalle_otra_enfermedad',
			'otras_enfermedades',
		]

		labels ={
			'fichas': 'Codigo Expediente y Numero de Ficha',
			'cambio_salud' : 'Cambio de Salud',
			'detalle_enf_operacion' : 'En que Consistio la enfermedad u operacion',
			'detalle_medicamento' : 'Medicamento Que ha tomado',
			'detalle_otra_enfermedad' : 'otras enfermedades',
			'otras_enfermedades': 'Tuvo alguna de estas enfermedades ',
		}
		widgets={
			'fichas':forms.HiddenInput(attrs={'class':'form-control','readonly':True}),
			'cambio_salud':forms.CheckboxInput(attrs={'disabled':True}),
			'detalle_enf_operacion':forms.Textarea(attrs={'class':'form-control','readonly':True}),
			'detalle_medicamento':forms.TextInput(attrs={'class':'form-control','readonly':True}),
			'detalle_otra_enfermedad':forms.TextInput(attrs={'class':'form-control','readonly':True}),
			'otras_enfermedades': forms.CheckboxSelectMultiple(attrs={'disabled':True}),
		}