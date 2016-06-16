
"""Gabriela URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url

from .views import (
	Inicio,
	Blog,
	Login,
	Institucional,
	Noticias,
	Contacto,
	Crear_Post,
	Detalle_Post,
	listar_post,
	act_post,
	eliminar_post,
	) 

#from . import views

urlpatterns = [

#----------> Pagina de Inicio de la Institución
	url(r'^$', Inicio.as_view(), name = 'Inicio' ),
	url(r'^institucional/$', Institucional.as_view(), name = 'Institucional' ),
	url(r'^contacto/$', Contacto.as_view(), name = 'Contacto' ),
	url(r'^noticias/$', Noticias.as_view(), name = 'Noticias' ),
	url(r'^blog/$', Blog.as_view(), name = 'Blog' ),
	url(r'^login/$', Login.as_view(), name = 'Login'),

#----------> CRUD del Blog

	url(r'^blog/nueva_entrada/$', Crear_Post, name='Crear'),
	url(r'^blog/detalle/$', Detalle_Post.as_view(), name='Detalle'),
	url(r'^blog/listar_entradas/$', listar_post.as_view(), name='Listar'),
	url(r'^blog/actualizar_entrada/$', act_post, name='Actualizar'),
	url(r'^blog/eliminar_entrada/$', eliminar_post, name='Eliminar'),



]

