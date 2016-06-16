from django.db import models
#Slugify permite trabajar con el slug
from django.template.defaultfilters import slugify
#Se importa el Settings para poder acceder al modelo usuario
from django.conf import settings

#Modelos pertenecientes a la App Inicio
	#Pagina de Inicio
	#Blog

class MarcaDeTiempo(models.Model):

#Esta lase abstracta me permitira registrar la creacion y modificación
#de las instancias sin necesidad de repitir los campos en cada modelo
	creacion = models.DateTimeField(auto_now_add=True)
	modificado = models.DateTimeField(auto_now=True)

	#Esto indica que este modelo no será una tabla en la base de datos,
	#sino una clase abstracta
	class Meta:
		abstract = True

#Modelo para la categorias del Blog
class Categoria(models.Model):

	nombre = models.CharField(max_length=50, unique=True, blank=False, null=False)
	slug = models.SlugField(editable=False)

	class Meta:
		verbose_name='Categoria (Blog)'
		verbose_name_plural ='Categorias (Blog)'

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.nombre)
		super(Categoria, self).save(*args, **kwargs)

	#para retornar el nombre cada que se muestre una referencia en la pantalla
	def __str__(self):
		return ('%s') %(self.nombre)

#Modelo para las Etiquetas de las entradas del Blog
class Tag(models.Model):

	nombre = models.CharField(max_length=50, unique=True, blank=False, null=False)
	slug = models.SlugField(editable=False)

	class Meta:
        	verbose_name = "Etiqueta  (Blog)"
        	verbose_name_plural = "Etiquetas  (Blog)"

	def save(self, *args, **kwargs):
			if not self.id:
				self.slug = slugify(self.nombre)
			super(Tag, self).save(*args, **kwargs)

	def __str__(self):
			return ('%s') %(self.nombre)

#Modelo para las entradas del Blog
class Post(MarcaDeTiempo):

	autor= models.ForeignKey(settings.AUTH_USER_MODEL)
	titulo = models.CharField('Título de la Entrada',max_length=200)
	contenido = models.TextField()
	imagen = models.ImageField(upload_to = 'Blog/entradas', blank=True, null=True)
	slug = models.SlugField(editable=False)
	publicar = models.BooleanField(default=False)
	categoria = models.ManyToManyField(Categoria)
	tags = models.ManyToManyField(Tag)

	class Meta:
	    verbose_name = "Entrada  (Blog)"
	    verbose_name_plural = "Entradas  (Blog)"
		    
	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.titulo)
		super(Post, self).save(*args, **kwargs)

	def __str__(self):
		return ('%s') %(self.titulo)


class Comentario_blog(MarcaDeTiempo):

	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	post = models.ForeignKey(Post)
	#Contenido del comentario
	contenido = models.TextField()

	class Meta:
		verbose_name='Comentario  (Blog)'
		verbose_name_plural ='Comentarios  (Blog)'

	#Retorno el usuario y el nombre del evento
	def __str__(self):
		return ('%s %s') %(self.user.username, self.post.titulo)

