from django.contrib import admin
from .models import Naipe, Instrumento, Musico

class MusicoAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            "Dados Pessoais:",
            {
                "fields" : ['nome','data_nascimento', 'foto'],
            }
        ),
        (
            "Dados Profissionais:",
            {
                "fields" : ['data_ingresso', 'naipe', 'instrumento', 'voz']
            }
        )
    ]
    list_display = ['nome', 'naipe', 'instrumento']
    list_filter = ['naipe', 'instrumento']
    ordering = ['naipe', 'instrumento', 'nome']
    search_fields = ['nome']
    actions_on_bottom = True
    actions_on_top = False

# Register your models here.
admin.site.register(Naipe)
admin.site.register(Instrumento)
admin.site.register(Musico, MusicoAdmin)
