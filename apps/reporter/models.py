from django.db import models


class Reporter(models.Model):
    nome_completo = models.CharField(max_length=70)

    def __str__(self):
        return self.nome_completo
