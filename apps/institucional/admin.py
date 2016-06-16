from django.contrib import admin

# Register your models here.
from .models import Contenido, Comentario, Categoria_f, Publicacion, Respuesta, Event, Category, Assistant, Comments

#-------------->  Material Educativo  <--------------

@admin.register(Contenido)
class ContenidoAdmin(admin.ModelAdmin):

	list_display = ('titulo', 'autor')
	list_filter = ('autor', 'materia', 'grado', )
	search_fields = ('titulo', 'contenido')
	ordering = ('titulo',)

	fieldsets = (
		('Contenido', {'fields' : (
			'autor', 
			'titulo',
			'contenido',
			'publicar',
			'materia',
			'grado',
			)}),
	)


@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):

	list_display = ('contenido', 'user')
	list_filter = ('user', 'contenido',)
	search_fields = ('user', 'contenido')
	ordering = ('creacion',)

	fieldsets = (
		('Usuario', {'fields' : (
			'user',
			)}),

		('Contenido', {'fields' : (
			'contenido',
			)}),

		('Comentario', {'fields' : (
			'comentario',
			)}),
	)


#-------------->  Foros  <--------------
admin.site.register(Categoria_f)

@admin.register(Publicacion)
class PublicacionAdmin(admin.ModelAdmin):

	list_display = ('titulo', 'autor',)
	list_filter = ('autor', 'categoria',)
	search_fields = ('autor', 'titulo', 'publicacion')
	ordering = ('creacion',)


@admin.register(Respuesta)
class RespuestaAdmin(admin.ModelAdmin):

	list_display = ('publicacion', 'usuario')
	list_filter = ('usuario', 'publicacion',)
	search_fields = ('usuario', 'publicacion')
	ordering = ('creacion',)

	fieldsets = (
		('Usuario', {'fields' : (
			'usuario',
			)}),

		('Publicación', {'fields' : (
			'publicacion',
			)}),

		('Respuesta', {'fields' : (
			'respuesta',
			)}),
	)



#-------------->  Eventos  <--------------

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):

	list_display = ('name', 'category', 'place', 'start', 'organizer')
	list_filter = ('category', 'place', 'organizer', )
	search_fields = ('name',)
	ordering = ('name',)

admin.site.register(Category)

@admin.register(Assistant)
class AssistantAdmin(admin.ModelAdmin):

	list_display = ('assistant',)
	list_filter = ('assistant', 'event',)
	search_fields = ('assistant', 'event')
	ordering = ('assistant',)

	fieldsets = (
		('Usuario', {'fields' : (
			'assistant',
			)}),

		('Evento', {'fields' : (
			'event', 
			'attended',
			'has_paid',
			)}),

	)


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):

	list_display = ('user', 'event')
	list_filter = ('user', 'event',)
	search_fields = ('user', 'event')
	ordering = ('creacion',)

	fieldsets = (
		('Usuario', {'fields' : (
			'user',
			)}),

		('Evento', {'fields' : (
			'event',
			)}),

		('Contenido', {'fields' : (
			'content',
			)}),
	)