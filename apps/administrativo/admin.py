from django.contrib import admin

from .models import (
	User, 
	Area,
	Seccion,
	Grado,
	Representante,
	Estudiante,
	Docente,
	Historial_docente,
	Materia,
	Horas_docente,
	Credencial_docente,
	)


#Usuario de la Aplicación
@admin.register(User)
class UserAdmin(admin.ModelAdmin):

	list_display = ('username', 'first_name', 'last_name', 'email')
	list_filter = ('is_active', )
	search_fields = ('username', 'email')
	ordering = ('username',)
	filter_horizontal = ('user_permissions',)

	fieldsets = (
		('User', {'fields' : (
			'username', 
			'password',
			)}),

		('Personal Info', {'fields' : (
			'first_name', 
			'last_name',
			'email',
			'avatar',
			)}),

		('Permissions', {'fields' : (
			'is_active', 
			'is_staff',
			'is_superuser',
			'groups',
			'user_permissions',
			)}),
	)


#Registros pertinentes a las inscripciones
@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):

	list_display = ('nombre',)
	ordering = ('nombre',)


@admin.register(Seccion)
class SeccionAdmin(admin.ModelAdmin):

	list_display = ('letra',)
	ordering = ('letra',)

	
@admin.register(Grado)
class GradoAdmin(admin.ModelAdmin):
	list_display = ('grado', 'seccion')
	list_filter = ('grado', 'seccion', 'area',)
	ordering = ('grado', 'seccion')


@admin.register(Docente)
class DocenteAdmin(admin.ModelAdmin):

	list_display = ('nombre', 'apellido', 'cargo')
	list_filter = ('cargo', 'grado',)
	search_fields = ('nombre', 'apellido', 'cargo', 'grado')
	ordering = ('apellido',)

	fieldsets = (
		('Datos personales', {'fields' : (
			'nombre',
			'apellido',
			'tipo_cedula',
			'cedula',
			'genero',
			'fecha_nac',
			'direccion',
			'tlf_fijo',
			'tlf_celular',
			'correo',
			'nacionalidad_o',
			'nacionalidad_act',
			)}),

		('Cargo', {'fields' : (
			'cargo',
			'grado',
			)}),
	)


@admin.register(Credencial_docente)
class Credencial_docenteAdmin(admin.ModelAdmin):

	list_display = ('docente', 'titulo', 'numero', 'fecha', 'institucion_o')
	list_filter = ('docente', 'institucion_o',)
	search_fields = ('docente', 'titulo', 'institucion_o')
	ordering = ('docente',)

	fieldsets = (
		('Credenciales', {'fields' : (
			'docente',
			'titulo',
			'numero',
			'fecha',
			'institucion_o',
			)}),
	)


@admin.register(Horas_docente)
class Horas_docenteAdmin(admin.ModelAdmin):

	list_display = ('docente', 'materia', 'grado', 'hora_semanal')
	list_filter = ('docente', 'materia', 'grado',)
	search_fields = ('docente', 'materia',)
	ordering = ('docente',)

	fieldsets = (
		('Horas por grado curso y asignatura', {'fields' : (
			'docente',
			'materia',
			'grado',
			'hora_semanal',
			)}),
	)


@admin.register(Historial_docente)
class Historial_docente(admin.ModelAdmin):

	list_display = ('docente', 'fecha_inicio')
	list_filter = ('docente', 'fecha_inicio',)
	search_fields = ('docente',)
	ordering = ('docente',)

	fieldsets = (
		('Historial Docente', {'fields' : (
			'docente',
			'estudio_act',
			'fecha_ce',
			'plantel_ce',
			'fecha_inicio',
			'educ_oficial_a',
			'educ_oficial_m',
			'educ_privada_a',
			'educ_privada_m',
			'total_servicio_a',
			'total_servicio_m',
			'observaciones',
			)}),
	)

@admin.register(Representante)
class RepresentanteAdmin(admin.ModelAdmin):

	list_display = ('nombre', 'apellido')
	list_filter = ('nombre', 'apellido',)
	search_fields = ('nombre', 'apellido',)
	ordering = ('apellido',)

	fieldsets = (
		('Datos personales', {'fields' : (
			'nombre',
			'apellido',
			'tipo_cedula',
			'cedula',
			'genero',
			'fecha_nac',
			'tlf_oficina',
			'tlf_celular',
			'correo',
			'ocupacion',
			)}),
		('Relacion con el estudiante', {'fields' : (
			'parentesco',
			)}),
	)


@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):

	list_display = ('nombre', 'apellido')
	list_filter = ('grado',)
	search_fields = ('nombre', 'apellido',)
	ordering = ('apellido',)

	fieldsets = (
		('Datos personales', {'fields' : (
			'nombre',
			'apellido',
			'tipo_cedula',
			'cedula',
			'genero',
			'fecha_nac',
			'lugar_nac',
			'estado',
			'direccion',
			'plantel_ant',
			'localidad',
			)}),
		('Información Académica', {'fields' : (			
			'grado',
			)}),
		('Representantes', {'fields' : (
			'representante',
			'madre',
			'cedula_m',
			'profesion_m',
			'padre',
			'cedula_p',
			'profesion_p',
			'convive',
			'convive_o',
			)}),
		('Salud', {'fields' : (			
			'enfermedad_hp',
			'enfermedad_padece',
			'alergico',
			'alergias',
			)}),
	)


@admin.register(Materia)
class MateriaAdmin(admin.ModelAdmin):
	list_display = ('nombre',)
	list_filter = ('grado', 'docente',)	
	search_fields = ('nombre', 'resumen', 'detalle')
	ordering = ('nombre',)
