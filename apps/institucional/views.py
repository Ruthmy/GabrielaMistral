from django.shortcuts import render

from django.views.generic import TemplateView

from .models import Event, Category, Assistant


# Create your views here.
class Eventos(TemplateView):
	template_name = 'institucional/eventos.html'

	def get_context_data(self, **kwargs):            
        	context = super(Eventos, self).get_context_data(**kwargs)
        	context['ultimos'] = Event.objects.all()[:5]
        	context['categorias'] = Category.objects.all()
        	context['asistentes'] = Assistant.objects.all()
        	return context


#Para los For con estos contextos utilizas el nombre del modelo
#{% for Event in ultimos %}		
#	<p>{{Event.name}}</p>
#{% endfor %}
