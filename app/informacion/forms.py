from django import forms
from app.informacion.models import estado_general,fichas,datos_generales
from django.contrib.admin import widgets
from django.contrib.admin.widgets import AdminDateWidget


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


class DatosGeneralesForm(forms.ModelForm):
	class Meta:
		model = datos_generales

		fields = [
			'cod_expediente',
			'nombre_completo',
			'edad',
			'edad_registro',
			'fecha_nac',
			'telefono',
			'genero',
			'direccion',
			'nombre_resp',
			'motivo_consulta',
			'fechaRegistro',
			#'usuario_creador',
			'fecha_hora_creacion',
		]

		labels={
			'cod_expediente':'Codigo Expediente',
			'nombre_completo':'Nombre Completo',
			'edad':'Edad Actual',
			'edad_registro':'Edad Registro',
			'fecha_nac':'Fecha de Nacimiento',
			'telefono':'Telefono',
			'genero':'Genero',
			'direccion':'Direccion',
			'nombre_resp':'Nombre del Padre o Encargado',
			'motivo_consulta':'Motivo de Consulta',
			'fechaRegistro':'Fecha de Registro',
			#'usuario_creador':'Nombre y Carne del creador',
			'fecha_hora_creacion':'Fecha y hora de creacion',
		}

		widgets={
			'cod_expediente':forms.TextInput(attrs={'class':'form-control'}),
			'nombre_completo':forms.TextInput(attrs={'class':'form-control'}),
			'edad':forms.TextInput(attrs={'class':'form-control'}),
			'edad_registro':forms.NumberInput(attrs={'class':'form-control'}),

			'fecha_nac':forms.DateInput(attrs={'class':'form-control'}),

			'telefono':forms.TextInput(attrs={'class':'form-control'}),
			'genero':forms.NumberInput(attrs={'class':'form-control'}),
			'direccion':forms.TextInput(attrs={'class':'form-control'}),
			'nombre_resp':forms.TextInput(attrs={'class':'form-control'}),
			'motivo_consulta':forms.Textarea(attrs={'class':'form-control'}),
			'fechaRegistro':forms.DateInput(attrs={'class':'form-control'}),
			#'usuario_creador':forms.TextInput(attrs={'class':'form-control'}),
			'fecha_hora_creacion':forms.DateInput(attrs={'class':'form-control'}),
		
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


class DatosGeneralesForm_consultars(forms.ModelForm):
	class Meta:
		model = datos_generales

		fields = [
			'cod_expediente',
			'nombre_completo',
			'edad',
			'edad_registro',
			'fecha_nac',
			'telefono',
			'genero',
			'direccion',
			'nombre_resp',
			'motivo_consulta',
			'fechaRegistro',
			#'usuario_creador',
			'fecha_hora_creacion',
		]

		labels={
			'cod_expediente':'Codigo Expediente',
			'nombre_completo':'Nombre Completo',
			'edad':'Edad Actual',
			'edad_registro':'Edad Registro',
			'fecha_nac':'Fecha de Nacimiento',
			'telefono':'Telefono',
			'genero':'Genero',
			'direccion':'Direccion',
			'nombre_resp':'Nombre del Padre o Encargado',
			'motivo_consulta':'Motivo de Consulta',
			'fechaRegistro':'Fecha de Registro',
			#'usuario_creador':'Nombre y Carne del creador',
			'fecha_hora_creacion':'Fecha y hora de creacion',
		}

		widgets={
			'cod_expediente':forms.TextInput(attrs={'class':'form-control','readonly':True}),
			'nombre_completo':forms.TextInput(attrs={'class':'form-control','readonly':True}),
			'edad':forms.TextInput(attrs={'class':'form-control','readonly':True}),
			'edad_registro':forms.NumberInput(attrs={'class':'form-control','readonly':True}),

			'fecha_nac':forms.DateInput(attrs={'class':'form-control','readonly':True}),

			'telefono':forms.TextInput(attrs={'class':'form-control','readonly':True}),
			'genero':forms.NumberInput(attrs={'class':'form-control','readonly':True}),
			'direccion':forms.TextInput(attrs={'class':'form-control','readonly':True}),
			'nombre_resp':forms.TextInput(attrs={'class':'form-control','readonly':True}),
			'motivo_consulta':forms.Textarea(attrs={'class':'form-control','readonly':True}),
			'fechaRegistro':forms.DateInput(attrs={'class':'form-control','readonly':True}),
			#'usuario_creador':forms.TextInput(attrs={'class':'form-control','readonly':True}),
			'fecha_hora_creacion':forms.DateInput(attrs={'class':'form-control','readonly':True}),
		
		}
		