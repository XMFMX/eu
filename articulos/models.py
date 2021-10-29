from django.db import models


class TSM(models.Model):
    tipo = models.CharField(null=True, blank=True, max_length=100)
    subtipo = models.CharField(null=True, blank=True, max_length=100)
    marca = models.CharField(null=True, blank=True, max_length=100)

    def __str__(self):
        return '{} {} {}'.format(self.tipo, self.subtipo, self.marca)
