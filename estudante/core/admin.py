from django.contrib import admin
from core.models import Estudante

class EstudanteAdmin(admin.ModelAdmin):

    list_display = ('name','telefone','course','create_at','update_at')
    search_fields = ['name']


admin.site.register(Estudante,EstudanteAdmin)
