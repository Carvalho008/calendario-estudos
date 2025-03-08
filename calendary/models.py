from django.db import models

class Estudo(models.Model):
    nome = models.CharField(max_length=200)
    tempo = models.FloatField()  # Tempo em horas

    def __str__(self):
        return f"{self.nome} - {self.tempo}h"

class DiaDeEstudo(models.Model):
    data = models.DateField(unique=True)
    estudos = models.ManyToManyField(Estudo, related_name="dias_de_estudo")

    @property
    def total_horas(self):
        return sum(estudo.tempo for estudo in self.estudos.all())

    @property
    def nivel(self):
        if self.total_horas > 8:
            return "green"
        elif self.total_horas > 5:
            return "yellow"
        return "red"

    def __str__(self):
        return f"{self.data} - {self.total_horas}h ({self.nivel})"
