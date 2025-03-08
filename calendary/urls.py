from django.urls import path
from .views import lista_dias_de_estudo

urlpatterns = [
    path('', lista_dias_de_estudo, name='dias_de_estudo'),
]
