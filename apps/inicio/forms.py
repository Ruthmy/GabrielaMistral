from django import forms

from .models import Post


#Defino el formulario
#Creo un campo por cada elemento que conformara el formulario
class Crear_PostForm(forms.ModelForm):

	class Meta:
		model = Post
		fields = ('titulo', 'contenido', 'imagen', 'publicar')
		exclude = ('autor', 'slug', 'tag')
		widgets = {
			'titulo' : forms.TextInput(attrs={'class':'form-control', 'placeholder' : 'Ingrese aqui el título'}),
			'contenido' : forms.Textarea(attrs={'class':'form-control', 'placeholder' : 'Escriba el cuerpo de la publicación'}),
			#'categoria' : forms.SelectMultiple([]),
			#ModelMultipleChoiceField, self).__init__(queryset, None,
            #required, widget, label, initial, help_text, *args, **kwargs)
			'imagen' : forms.FileInput(),
		}






