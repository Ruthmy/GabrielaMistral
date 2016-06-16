from django.db import models
#Con estas tres clases puedo crear un modelo de usuario personalizado
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

#Modelos pertenecientes a la app Administrativo
	#Usuario Personalizado
	#Estudiantes
	#Representantes
	#Docentes
	#Grado
	#Seccion
	#Materias
	#Horario (Pendiente)


#Manager para el modelo User
class UserManager(BaseUserManager, models.Manager):

	#Definicion del metodo para crear un usuario
	def _create_user(self, username, email, password, is_staff, is_superuser, **extra_fields):

		#El metodo normalize_email pasa a minusculas el dominio del email
		email = self.normalize_email(email)
		#Aqui lanzo el error en caso de que no sea un email
		if not email:
			#Levanto un error de validacion
			raise ValueError('El email debe ser obligatorio')
		
		#variable user que sera el modelo
		user = self.model(username = username, email = email, is_active = True, is_staff = is_staff, is_superuser = is_superuser, **extra_fields)

		#setear el password
		user.set_password(password)
		#Guardo al usuario en la base de datos
		user.save(using = self._db)

		return user


	#Función para crear un usuario
	def create_user(self, username, email, password=None, **extra_fields):
		return self._create_user(username, email, password, False, False, **extra_fields)

	#Función para crear un superusuario
	def create_superuser(self, username, email, password=None, **extra_fields):
		return self._create_user(username, email, password, True, True, **extra_fields)

#Este es el modelo del AUTH_USER_MODEL
class User(AbstractBaseUser, PermissionsMixin):

	username = models.CharField(max_length=100, unique=True)
	email = models.EmailField()
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	#Foto del usuario
	avatar = models.ImageField(upload_to = 'media/users', null=True, blank=True)
	
	#Los usuarios personalizados deben tener un Manager
	objects = UserManager()

	#Si el usuario esta o no activo
	is_active = models.BooleanField(default=True)
	#
	is_staff = models.BooleanField(default=False)


	#Esto es para que un superusuario se pueda logear con su username
	USERNAME_FIELD = 'username'
	#Campos requeridos cuando se quiera crear un superusuario
	REQUIRED_FIELDS = ['email']

	def get_short_name(self):
		return ('%s') %(self.username)

	def get_full_name(self):
		return ('%s') %(self.username)



#--------------------------->  Area Gradoy Seccion  <----------------------------
class Area(models.Model):

	nombre = models.CharField(max_length=50, default='', unique=True, blank=False, null=False)

	class Meta:
    		verbose_name = "Área"    
    		verbose_name_plural = "Áreas"

	def __str__(self):
			return ('%s') %(self.nombre)

class Seccion(models.Model):

	#Busca como pasar la letra ingresada a mayusulas
	letra = models.CharField(max_length=1,default='', unique=True, blank=False, null=False)

	class Meta:
        	verbose_name = "Sección"
        	verbose_name_plural = "Secciones"

	def __str__(self):
			return ('%s') %(self.letra)

class Grado(models.Model):

	area = models.ForeignKey(Area)
	grado = models.CharField(max_length=50, default='', blank=False, null=False)
	seccion = models.ForeignKey(Seccion)

	#Como puedes hacer que sea unico?

	class Meta:
        	verbose_name = "Grado"
        	verbose_name_plural = "Grados"

	def __str__(self):
			return ('%s %s') %(self.grado, self.seccion)

#----------------------------->  Modelo Personas  <--------------------------------

class Persona(models.Model):

	nombre = models.CharField(max_length=100, blank=False, null=False)
	apellido = models.CharField(max_length=100, blank=False, null=False)
	choices = (
		('V' , 'Venezolano'),
		('E' , 'Extranjero'),
		)
	tipo_cedula = models.CharField(max_length=1, default='V', choices= choices, blank=True, null=True)
	#Verifica con una funciono con el formulario que cedula sea unica
	#y tenga minimo y max de caracteres
	cedula = models.CharField(max_length=50, blank=True, null=True)
	choices = (
		('M' , 'Masculino'),
		('F' , 'Femenino'),
		)
	genero = models.CharField(max_length=1, default='F', choices= choices, blank=False, null=False)
	
	#Debes arreglar la fecha de nacimiento
	#Lo ideal es que puedas poner un formato de dia mes y año
	fecha_nac = models.DateField()

	creacion = models.DateTimeField(auto_now_add=True)
	modificado = models.DateTimeField(auto_now=True)

	#Esto indica que este modelo no será una tabla en la base de datos,
	#sino una clase abstracta
	class Meta:
		abstract = True

#----------------------------->  Modelo Representante  <--------------------------------

class Representante(Persona):

	tlf_oficina = models.CharField(max_length=100, blank=True, null=True)
	tlf_celular = models.CharField(max_length=100, blank=True, null=True)
	correo = models.EmailField(max_length=254, unique=True, blank=True, null=True)
	#Parentesco con el Estudiante
	ocupacion = models.CharField(max_length=100, blank=True, null=True)
	parentesco = models.CharField(max_length=50, blank=False, null=False)

	class Meta:
        	verbose_name = "Representante"
        	verbose_name_plural = "Representantes"

	def __str__(self):
			return ('%s %s') %(self.apellido, self.nombre)
    
#----------------------------->  Modelo Estudiante  <----------------------------

class Estudiante(Persona):

	#AGREGALE CORREO
	#ME SUPONGO QUE SIN EL NO PODRA INICIAR SESION EN LA PLATAFORMA
	#correo = models.EmailField(max_length=254, unique=True, blank=True, null=True)
	cedula_esc = models.CharField('Cedula Escolar', max_length=11, blank=True, null=True)
	lugar_nac = models.CharField(max_length=200, blank=False, null=False)
	estado = models.CharField(max_length=100, blank=False, null=False)
	direccion = models.TextField()

	representante = models.ForeignKey(Representante)
	madre = models.CharField(max_length=200, blank=True, null=True)
	cedula_m = models.CharField(max_length=50, blank=True, null=True)
	profesion_m = models.CharField(max_length=50, blank=True, null=True)
	padre = models.CharField(max_length=200, blank=True, null=True)
	cedula_p = models.CharField(max_length=50, blank=True, null=True)
	profesion_p = models.CharField(max_length=50, blank=True, null=True)
	#Con quien convive el estudiante
	choices = (
		('Padre' , 'Padre'),
		('Madre' , 'Madre'),
		('Ambos' , 'Ambos'),
		)
	convive = models.CharField(max_length=5, default='Ambos', choices= choices, blank=True, null=True)
	convive_o = models.CharField(max_length=50, blank=True, null=True)
	#Plantel anterior (en caso de provenir de otra institucion)
	plantel_ant = models.CharField(max_length=100, blank=True, null=True)
	#direccion del plantel anterio
	localidad = models.CharField(max_length=100, blank=True, null=True)

	grado = models.ForeignKey(Grado)	

	#Piensa en como puedes añadirle el año escolar
	#Que lo registres con la inscripcion y que sea acumulativo
	#en lainscripcion siguiente debe reflejarse en el documento
	#el periodo escolar del año anterior

	enfermedad_hp = models.TextField('Enfermedad que ha padecido', default='Ninguna')
	enfermedad_padece = models.TextField('Enfermedad que padece', default='Ninguna')
	alergico  = models.TextField('Alérgico a Medicamento', default='Ninguno')
	alergias = models.TextField('Alergia', default='Ninguna')

	class Meta:
        	verbose_name = "Estudiante"
        	verbose_name_plural = "Estudiantes"

	def __str__(self):
			return ('%s %s %s') %(self.apellido, self.nombre, self.grado)


  
#---------------------->  Modelos para Maestros y Profesores  <--------------------

class Docente(Persona):

	direccion = models.TextField(blank=False, null=False)
	tlf_fijo = models.CharField(max_length=100, blank=True, null=True)
	tlf_celular = models.CharField(max_length=100, blank=True, null=True)
	correo = models.EmailField(max_length=254, unique=True, blank=True, null=True)
	nacionalidad_o = models.CharField('Nacionalidad originaria', default='Venezolano', max_length=100, blank=False, null=False)
	nacionalidad_act = models.CharField('Nacionalidad actual', default='Venezolano', max_length=100, blank=False, null=False)
	cargo = models.CharField(max_length=100, blank=False, null=False)
	#En en modelo grado ya se asgna el area
	#area = models.ManyToManyField(Area)
	grado = models.ManyToManyField(Grado)
	#horas = models.CharField(max_length=10, default='1', blank=False, null=False)

	#Como colocar que es un profesor guia?

	#historial = models.OneToOneField(Historial_docente)
    
	class Meta:
        	verbose_name = "Profesor"
        	verbose_name_plural = "Profesores"
    
	def __str__(self):
			return ('%s %s') %(self.apellido, self.nombre)       


class Historial_docente(models.Model):

	docente = models.OneToOneField(Docente)
	#Indicacion de si estudia actualmente o no y que estudia
	estudio_act = models.TextField()
	#Fecha en que inicia el ejercicio docente
	fecha_ce = models.DateField()
	#Plantel en que inicia el ejercicio docente
	plantel_ce = models.CharField('Plantel en que comenzó a ejercer', max_length=100, blank=False, null=False)
	#Fecha en que comenzo a trabajar en la Gabriela
	fecha_inicio = models.DateField()
	#Tiempo de servicio
	educ_oficial_a = models.CharField(max_length=50, blank=False, null=False)
	educ_oficial_m = models.CharField(max_length=50, blank=False, null=False)
	educ_privada_a = models.CharField(max_length=50, blank=False, null=False)
	educ_privada_m = models.CharField(max_length=50, blank=False, null=False)
	total_servicio_a = models.CharField(max_length=50, blank=False, null=False)
	total_servicio_m = models.CharField(max_length=50, blank=False, null=False)

	observaciones = models.TextField()


	class Meta:
        	verbose_name = "Historial"
        	verbose_name_plural = "Historiales"
    
	def __str__(self):
			return ('%s') %(self.docente)


#----------------------------->  Modelo Materia  <----------------------------

class Materia(models.Model):

	nombre = models.CharField(max_length=100, blank=False, null=False)
	#Resumen de la materia
	resumen = models.TextField()
	#Detalle de los temas que componen la materia
	detalle = models.TextField()
	#Grado en que se imparte la materia
	grado = models.ManyToManyField(Grado)
	#Docente o Docentes que imparten la materia
	docente = models.ManyToManyField(Docente)

	class Meta:
        	verbose_name = "Materia"
        	verbose_name_plural = "Materias"
    
	def __str__(self):
			return ('%s') %(self.nombre)


class Horas_docente(models.Model):

	docente = models.ForeignKey(Docente)
	materia = models.ForeignKey(Materia)
	#Por la manera en que esta hecho, se muestra grado y seccion con llamar al
	#objeto grado Ve si puedes o corregirlo o llamarlo por partes
	grado = models.ForeignKey(Grado)
	hora_semanal = models.CharField(max_length=10, blank=False, null=False)
	#El total de horas semanales creo que tendra que ir a parte
	#Una variable temporal o un algo que sume todos los hora_semanal

	class Meta:
	        verbose_name = "Horas docente"
	        verbose_name_plural = "Horas docentes"

	def __str__(self):
	        	return ('%s') %(self.docente)

class Credencial_docente(models.Model):

	docente = models.ForeignKey(Docente)
	titulo = models.CharField(max_length=200, blank=False, null=False)
	numero = models.CharField(max_length=50, blank=False, null=False)
	fecha = models.DateField()
	#Insitucion que otorga el titulo
	institucion_o = models.CharField(max_length=200, blank=False, null=False)

	class Meta:
	        verbose_name = "Credencial docente"
	        verbose_name_plural = "Credenciales docentes"

	def __str__(self):
        	return ('%s') %(self.docente)
    


