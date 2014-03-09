from django.contrib import admin
from models import codeProgramme, codeCours, Etablissement, Professeur, Cours

# Register your models here.

class ProfesseurAdmin (admin.ModelAdmin):
    list_display = ('nom','prenom','no_identite')

class CourAdmin (admin.ModelAdmin):
    list_display = ('lieu','planducours','objectifs')

class EtablissementAdmin (admin.ModelAdmin):
    list_display = ('nom','lieu',)


admin.site.register(codeProgramme)
admin.site.register(codeCours)
admin.site.register(Etablissement, EtablissementAdmin)
admin.site.register(Professeur, ProfesseurAdmin)
admin.site.register(Cours, CourAdmin)