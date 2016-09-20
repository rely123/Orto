from django import forms
from app.tipo_perfil.models import TipoPerfil,PerfilTotal,FacialFrontal
from app.tipo_perfil.models import Sonrisa,PTercioInferioir
#from app.informacion.models import datos_generales


class Tipo_perfilForm(forms.ModelForm):

	class Meta:
		model = TipoPerfil

		fields = [
			'id_tipo_perfil',
			#'cod_expediente',

			'id_frontal_facial', 
			'id_tipoPerfiltotal', 
			'id_perfilTercio_inferior', 
			'id_tipoSonrisa', 

			'tipoNariz', 
			'angulo_Naso_labial', 
			'tercio_superior', 
			'tercio_medio', 
			'tercio_inferior', 
			'tamanoSonrisa', 
			'grosorLabios',
			'tamanoLabios', 
			'tipo_competenciaLabial', 
		]

		labels = {
			'id_tipo_perfil': 'Codigo',
			#'cod_expediente': 'Codigo expediente',

			'id_frontal_facial': 'Facial Frontal',
			'id_tipoPerfiltotal': 'Perfil total', 
			'id_perfilTercio_inferior': 'Perfil 1/3 inferior', 
			'id_tipoSonrisa': 'Sonrisa',  

			'tipoNariz': 'Nariz',
			'angulo_Naso_labial': 'Angulo naso labial',
			'tercio_superior': 'Tercio Superior',
			'tercio_medio': 'Tercio Medio',
			'tercio_inferior': 'Tercio Inferior',
			'tamanoSonrisa': 'Tamano de Sonrisa',
			'grosorLabios': 'Grosor de labios',
			'tamanoLabios': 'Tamano de labios',
			'tipo_competenciaLabial': 'Competencia labial',

		}

		widgets = {
			'id_tipo_perfil': forms.TextInput(attrs={'class':'form-control'}),
			#'cod_expediente': forms.Select(attrs={'class':'form-control'}),

			'id_frontal_facial': forms.Select(attrs={'class':'form-control'}),
			'id_tipoPerfiltotal': forms.Select(attrs={'class':'form-control'}), 
			'id_perfilTercio_inferior': forms.Select(attrs={'class':'form-control'}), 
			'id_tipoSonrisa': forms.Select(attrs={'class':'form-control'}), 

			'tipoNariz': forms.TextInput(attrs={'class':'form-control'}),
			'angulo_Naso_labial': forms.TextInput(attrs={'class':'form-control'}),
			'tercio_superior': forms.TextInput(attrs={'class':'form-control'}),
			'tercio_medio': forms.TextInput(attrs={'class':'form-control'}),
			'tercio_inferior':forms.TextInput(attrs={'class':'form-control'}),
			'tamanoSonrisa':forms.TextInput(attrs={'class':'form-control'}),
			'grosorLabios':forms.TextInput(attrs={'class':'form-control'}),
			'tamanoLabios': forms.TextInput(attrs={'class':'form-control'}),
			'tipo_competenciaLabial': forms.TextInput(attrs={'class':'form-control'}),

		}


