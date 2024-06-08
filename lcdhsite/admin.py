from django.contrib import admin
from django.db.models import *
from django.views.decorators.vary import vary_on_cookie

from .models import Country, Celula, Anuncio, Compa, CategoriaProfesion, Profesion, AsistenciaCompaCelula
import json
from django.core.serializers.json import DjangoJSONEncoder


class CountryAdminDisplay(admin.ModelAdmin):
    prepopulated_fields = {'sectionname': ('name',)}

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['title'] = 'Seleccione el país a cambiar'
        return super().changelist_view(request, extra_context=extra_context)


class CompaAdminDisplay(admin.ModelAdmin):
    list_display = ('nickname', 'celula', 'edad', 'sexo')
    list_filter = ('celula',)
    search_fields = ('nickname',)
    list_per_page = 10

    @vary_on_cookie
    def changelist_view(self, request, extra_context=None):
        # aggregate Compa professions
        chart_data = (
            Compa.objects.annotate(Count("sexo", distinct=True),
                                   Count("profession__categoriaProfesion__name", distinct=True),
                                   Count("edad", distinct=True))
            .values("id", "sexo", "profession__categoriaProfesion__name", "edad")
            .order_by("-edad")
        )
        # Serialize and attach the chart data to the template context
        as_json = json.dumps(list(chart_data), cls=DjangoJSONEncoder)
        print("Json %s" % as_json)
        extra_context = extra_context or {"chart_data": as_json}
        extra_context['title'] = 'Seleccione el compa a cambiar'
        # Call the superclass changelist_view to render the page
        return super().changelist_view(request, extra_context=extra_context)


class CelulaAdminDisplay(admin.ModelAdmin):
    list_display = ('name', 'country', 'hideInMainPage')
    list_editable = ('hideInMainPage',)
    list_filter = ('country',)
    search_fields = ('name',)
    list_per_page = 15
    filter_horizontal = ('staff',)

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['title'] = 'Seleccione la célula a cambiar'
        return super().changelist_view(request, extra_context=extra_context)


class AnuncioAdminDisplay(admin.ModelAdmin):
    list_display = ('alt', 'celula')
    list_filter = ('celula',)
    search_fields = ('alt',)

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['title'] = 'Seleccione el anuncio a cambiar'
        return super().changelist_view(request, extra_context=extra_context)


class ProfesionAdminDisplay(admin.ModelAdmin):
    list_display = ('name', 'categoriaProfesion')

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['title'] = 'Seleccione la profesión a cambiar'
        return super().changelist_view(request, extra_context=extra_context)


class CategoriaProfesionAdminDisplay(admin.ModelAdmin):

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['title'] = 'Seleccione la categoría de profesión a cambiar'
        return super().changelist_view(request, extra_context=extra_context)


admin.site.register(Country, CountryAdminDisplay)
admin.site.register(Celula, CelulaAdminDisplay)
admin.site.register(Anuncio, AnuncioAdminDisplay)
admin.site.register(Compa, CompaAdminDisplay)
admin.site.register(CategoriaProfesion, CategoriaProfesionAdminDisplay)
admin.site.register(Profesion, ProfesionAdminDisplay)
admin.site.register(AsistenciaCompaCelula)
