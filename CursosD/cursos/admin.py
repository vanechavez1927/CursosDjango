from django.contrib import admin
from .models import Curso

class CursoAdmin(admin.ModelAdmin):
    readonly_fields = ('creado', 'actualizado')
    list_display = ('nombre', 'modalidad', 'duracion_horas', 'disponible')
    search_fields = ('nombre', 'modalidad', 'descripcion')
    date_hierarchy = 'creado'
    list_filter = ('modalidad', 'disponible',)

admin.site.register(Curso, CursoAdmin)
