#Importaciones de Django
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
#from django.views.generic import TemplateView, CreateView, DetailView, UpdateView, DeleteView

#Importaciones del proyecto
from .models import Post, Tag, Categoria
from apps.administrativo.models import Grado
from .forms import Crear_PostForm


#--------------------> Pagina de Inicio de la Institución <-----------------------

class Inicio(TemplateView):
    template_name = 'inicio/index.html'

    def get_context_data(self, **kwargs):
        context = super(Inicio, self).get_context_data(**kwargs)
        context['lastest'] = Post.objects.all()[:5]
        return context

#No funcional
class Institucional(TemplateView):
    template_name = 'inicio/institucional.html'

    def get_context_data(self, **kwargs):            
        context = super(Institucional, self).get_context_data(**kwargs)
        context['lastest'] = Post.objects.all()[:5]
        context['grados'] = Grado.objects.all()
        return context

#No funcional
class Login(TemplateView):
    template_name = 'inicio/login.html'

#No funcional
class Contacto(TemplateView):
    template_name = 'inicio/contacto.html'


class Prefooter(TemplateView):
    template_name = 'prefooter.html'

    def get_context_data(self, **kwargs):            
        context = super(Prefooter, self).get_context_data(**kwargs)
        context['lastest'] = Post.objects.all()[:5]
        return context

"""
def Prefooter(request):
    lastest_post = Post.objects.all()[:5]
    context = {'lastest_post': lastest_post}
    return render(request, 'templates/prefooter.html', context)
"""

#---------------------------> Blog de la Gabriela <------------------------------

class Noticias(TemplateView):
    template_name = 'blog/noticias.html'

    def get_context_data(self, **kwargs):            
        context = super(Noticias, self).get_context_data(**kwargs)
        #Aqui solo debes añadirle algun condicional de que deben ser de
        #la categoria noticias
        context['lastest_post'] = Post.objects.all().filter(categoria__nombre = 'Noticias')
        context['lastest'] = Post.objects.all()[:5]
        #En tags y categorias falta poner el enlace, creo q es con el slug
        context['tags'] = Tag.objects.all()
        context['categorias'] = Categoria.objects.all()
        return context



class Blog(TemplateView):
    template_name = 'blog/index_blog.html'

    def get_context_data(self, **kwargs):            
        context = super(Blog, self).get_context_data(**kwargs)
        context['lastest_post'] = Post.objects.all()[:5]
        context['lastest'] = Post.objects.all()[:5]
        #En tags y categorias falta poner el enlace, creo q es con el slug
        context['tags'] = Tag.objects.all()
        context['categorias'] = Categoria.objects.all()
        return context


#Aun no construida
#class Detalle(TemplateView):
#    template_name = 'blog/detalle.html'

#----------------> CRUD de las Entradas del Blog

def Crear_Post(request):

    if request.user.is_authenticated():        
        if request.method =="POST":
            form = Crear_PostForm(request.POST)
            if form.is_valid():
                #Validaciones
                print("IS_VALID")
                return redirect("/")
        else:
            form = Crear_PostForm()
    else:
        return redirect("/")

    return render(request, "blog/nueva_entrada.html", {"form" : form})


class Detalle_Post(TemplateView):
    template_name = 'blog/detalle.html'

    def get_context_data(self, **kwargs):            
        context = super(Detalle_Post, self).get_context_data(**kwargs)
        context['entrada'] = Post.objects.all()
        #En tags y categorias falta poner el enlace, creo q es con el slug
        context['tags'] = Tag.objects.all()
        context['categorias'] = Categoria.objects.all()
        return context

#context = {
    #"titulo" : "Hola Hola =D"
    #}
    #return render(request, "blog/detalle.html", context)

class listar_post(TemplateView):
    template_name = 'blog/listar_post.html'

    def get_context_data(self, **kwargs):            
        context = super(listar_post, self).get_context_data(**kwargs)
        context['listar_post'] = Post.objects.all()#[:5]
        #En tags y categorias falta poner el enlace, creo q es con el slug
        #context['tags'] = Tag.objects.all()
        #context['categorias'] = Categoria.objects.all()
        return context


def act_post(request):

        return HttpResponse("Actualizar un Post")

def eliminar_post(request):

        return HttpResponse("Eliminar Post")




