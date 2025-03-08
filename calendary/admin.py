from django.contrib import admin
from .models import DiaDeEstudo, Estudo

class NivelFilter(admin.SimpleListFilter):
    title = "Nível"
    parameter_name = "nivel"

    def lookups(self, request, model_admin):
        return [
            ("green", "Green (>8h)"),
            ("yellow", "Yellow (>5h)"),
            ("red", "Red (<5h)"),
        ]

    def queryset(self, request, queryset):
        if self.value() == "green":
            return queryset.filter(estudos__tempo__gt=8).distinct()
        elif self.value() == "yellow":
            return queryset.filter(estudos__tempo__gt=5, estudos__tempo__lte=8).distinct()
        elif self.value() == "red":
            return queryset.filter(estudos__tempo__lte=5).distinct()
        return queryset

@admin.register(Estudo)
class EstudoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tempo')

@admin.register(DiaDeEstudo)
class DiaDeEstudoAdmin(admin.ModelAdmin):
    list_display = ('data', 'total_horas', 'nivel')
    list_filter = (NivelFilter,)  # Usa o filtro personalizado
    ordering = ('data',)

    def total_horas(self, obj):
        return obj.total_horas
    total_horas.short_description = "Horas Totais"

    def nivel(self, obj):
        return obj.nivel
    nivel.short_description = "Nível"
