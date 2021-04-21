from django.db import models


class Medico(models.Model):
    ordenador = models.IntegerField()
    nome = models.CharField(max_length=200)
    especialidade = models.TextField()
