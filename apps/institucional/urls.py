from django.conf.urls import url

from .views import Eventos

urlpatterns = [

#----------> Pagina de Inicio de la Institución
	#url(r'^$', Inicio.as_view(), name = 'Inicio' ),
	url(r'^eventos/$', Eventos.as_view(), name = 'Eventos' ),
	#url(r'^contacto/$', Contacto.as_view(), name = 'Contacto' ),
	#url(r'^noticias/$', Noticias.as_view(), name = 'Noticias' ),
	#url(r'^blog/$', Blog.as_view(), name = 'Blog' ),
	#url(r'^login/$', Login.as_view(), name = 'Login'),


]