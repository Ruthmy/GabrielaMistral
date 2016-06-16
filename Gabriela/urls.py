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
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^', include('apps.inicio.urls')),
    url(r'^', include('apps.institucional.urls')),
    #url(r'^', include('apps.administrativo.urls')),    
    #url(r'^', include('apps.encuesta.urls')),

    #URLConfig de la aplicacion encuestas
    #url(r'^encuesta/', include('apps.encuesta.urls')),


]


"""
Recuerda que siempre que deberas usar el Include() siempre que agreges otro
archivo de configuracion de URLS diferente al archivo raiz
"""
