from django.contrib import admin

# Register your models here.

from .models import Categoria, Tag, Post, Comentario_blog

admin.site.register(Categoria)
admin.site.register(Tag)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

	list_display = ('titulo', 'autor', 'publicar', 'creacion')
	list_filter = ('autor', 'publicar', 'categoria',)
	search_fields = ('autor', 'titulo', )
	ordering = ('creacion',)


@admin.register(Comentario_blog)
class Comentario_blogAdmin(admin.ModelAdmin):

	list_display = ('post', 'user')
	list_filter = ('user', 'post',)
	search_fields = ('user', 'post')
	ordering = ('creacion',)

	fieldsets = (
		('Usuario', {'fields' : (
			'user',
			)}),

		('Post', {'fields' : (
			'post',
			)}),

		('Contenido', {'fields' : (
			'contenido',
			)}),
	)


