from django.db import models
from apps.reporter.models import Reporter


class Artigo(models.Model):
    data_publicacao = models.DateField()
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    reporter = models.ForeignKey(Reporter)

    def __str__(self):
        return self.headline
