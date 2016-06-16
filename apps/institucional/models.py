from django.db import models
from django.template.defaultfilters import slugify
#Se importa el Settings para poder acceder al modelo usuario
from django.conf import settings

# Modelos pertinentes a la app Institucional
	#Material Educativo
	#Foros
	#Eventos de la Institución

#-------------->  Material Educativo  <--------------
class MarcaDeTiempo(models.Model):

	creacion = models.DateTimeField(auto_now_add=True)
	actualizacion = models.DateTimeField(auto_now=True)

	class Meta:
		abstract = True


class Contenido(MarcaDeTiempo):

	autor= models.ForeignKey(settings.AUTH_USER_MODEL)
	titulo = models.CharField(max_length=200)
	contenido = models.TextField()
	slug = models.SlugField(editable=False)
	publicar = models.BooleanField(default=False)
	materia = models.ManyToManyField('administrativo.Materia')
	grado = models.ManyToManyField('administrativo.Grado')

	class Meta:
	    verbose_name = "Contenido (Material Educativo)"
	    verbose_name_plural = "Contenidos (Material Educativo)"
		    
	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.titulo)
		super(Contenido, self).save(*args, **kwargs)

	def __str__(self):
		return ('%s') %(self.titulo)


class Comentario(MarcaDeTiempo):

	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	contenido = models.ForeignKey(Contenido)
	#Contenido del comentario
	comentario = models.TextField()

	class Meta:
		verbose_name='Comentario (Material Educativo)'
		verbose_name_plural ='Comentarios (Material Educativo)'

	#Retorno el usuario y el nombre del evento
	def __str__(self):
		return ('%s %s') %(self.user.username, self.contenido.titulo)


#------------------------------->  Foros  <--------------------------------------

class Categoria_f(models.Model):

	#nombre de la categoria
	nombre = models.CharField(max_length=50)
	slug = models.SlugField(editable=False)

	class Meta:
		verbose_name='Categoria (Foro)'
		verbose_name_plural ='Categorias (Foro)'

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.nombre)
		super(Categoria_f, self).save(*args, **kwargs)

	def __str__(self):
		return ('%s') %(self.nombre)


class Publicacion(MarcaDeTiempo):

	autor = models.ForeignKey(settings.AUTH_USER_MODEL)
	titulo = models.CharField(max_length=200, blank=False, null=False)
	publicacion = models.TextField()
	categoria = models.ForeignKey(Categoria_f)
	slug = models.SlugField(editable=False)

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.titulo)
		super(Publicacion, self).save(*args, **kwargs)

	class Meta:
        	verbose_name = "Publicación (Foro)"
        	verbose_name_plural = "Publicaciones (Foro)"

	def __str__(self):
			return ('%s %s') %(self.titulo, self.autor.username)
    

class Respuesta(MarcaDeTiempo):

	usuario = models.ForeignKey(settings.AUTH_USER_MODEL)
	publicacion = models.ForeignKey(Publicacion)
	#Contenido del comentario
	respuesta = models.TextField()

	class Meta:
		verbose_name='Respuesta (Foro)'
		verbose_name_plural ='Respuestas (Foro)'

	#Retorno el usuario y el nombre del evento
	def __str__(self):
		return ('%s %s') %(self.usuario.username, self.publicacion.titulo)


#----------------------------->  Eventos  <---------------------------------------

class Category(models.Model):

	#nombre de la categoria
	name = models.CharField(max_length=50)
	slug = models.SlugField(editable=False)

	class Meta:
		verbose_name='Categoria (Eventos)'
		verbose_name_plural ='Categorias (Eventos)'

	#se define save para poder guardar el evento
	def save(self, *args, **kwargs):
		if not self.id:
			#utilizo el metodo slugify para crear el slug
			#y llenar el atributo slug segun el nombre
			self.slug = slugify(self.name)
		#para que el metodo save siga su camino normalmente
		super(Category, self).save(*args, **kwargs)

	#para retornar el nombre cada que se muestre una referencia en la pantalla
	def __str__(self):
		return ('%s') %(self.name)


class Event(MarcaDeTiempo):

	name = models.CharField(max_length=200, unique=True)
	slug = models.SlugField(editable=False)
	#resumen del evento
	summary = models.TextField(max_length=250)
	#contenido del evento
	content = models.TextField()
	#Llave foranea al modelo category
	category = models.ForeignKey(Category)
	place = models.CharField(max_length=50, default="Colegio")
	#fecha de inicio
	start = models.DateTimeField()
	#fin
	finish =models.DateTimeField()
	imagen = models.ImageField(upload_to = 'eventos', null=True, blank=True)
	#si es o no es gratis
	is_free = models.BooleanField(default=True)
	#costo
	#amount = models.DecimalField(max_digit=5, decimal_places=2, default=0.00)
	#cantidad de personas que han visto el evento
	views = models.PositiveIntegerField(default=0)
	#organizador del evento
	organizer = models.ForeignKey(settings.AUTH_USER_MODEL) #Falta el modelo user

	class Meta:
		verbose_name='Evento'
		verbose_name_plural ='Eventos'

	def save(self, *args, **kwargs):
		if not self.id:
			#utilizo el metodo slugify para crear el slug
			#y llenar el atributo slug segun el nombre
			self.slug = slugify(self.name)
		#para que el metodo save siga su camino normalmente
		super(Event, self).save(*args, **kwargs)

	def __str__(self):
		return ('%s') %(self.name)


#Asistentes
class Assistant(MarcaDeTiempo):

	assistant = models.ForeignKey(settings.AUTH_USER_MODEL)
	#Evento al que asistira
	#Un asistente puede ir a muchos eventos y un evento puede tener muchos asistentes
	event = models.ManyToManyField(Event)
	#si fue o no
	attended = models.BooleanField(default=False)
	#si pago por el evento
	has_paid = models.BooleanField(default=False)

	class Meta:
		verbose_name='Asistente (Eventos)'
		verbose_name_plural ='Asistentes (Eventos)'

	#En este caso se retornan dos string, el username de quien asistio
	#y el nombre del evento
	def __str__(self):
		return ('%s %s') %(self.assistant.username, self.event.name)


class Comments(MarcaDeTiempo):

	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	event = models.ForeignKey(Event)
	#Contenido del comentario
	content = models.TextField()

	class Meta:
		verbose_name='Comentario (Eventos)'
		verbose_name_plural ='Comentarios (Eventos)'

	#Retorno el usuario y el nombre del evento
	def __str__(self):
		return ('%s %s') %(self.user.username, self.event.name)


