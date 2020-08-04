from django.contrib import admin
from core.models import Estudante

class EstudanteAdmin(admin.ModelAdmin):

    list_display = ('nome','telefone','curso','create_at','update_at')
    search_fields = ['nome']


admin.site.register(Estudante,EstudanteAdmin)
