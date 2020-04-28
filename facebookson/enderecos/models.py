from django.db import models

# Create your models here.
class Endereco(models.Model):
    logradouro = models.CharField(max_length=255, blank=False, null=False)
    bairro = models.CharField(max_length=255, blank=False, null=False)
    cidade = models.CharField(max_length=255, blank=False, null=False)
    numero = models.IntegerField(max_length=20, blank=False, null=False)
    cep = models.CharField(max_length=10, blank=False, null=False)

    def __str__(self):
        return 'Rua ' + self.logradouro