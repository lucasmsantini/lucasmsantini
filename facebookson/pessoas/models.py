from django.db import models

# Create your models here.
class Telefone(models.Model):
    numero = models.CharField(max_length=13, null=False, blank=False)
    def __str__(self):
        return self.numero

class Pessoa(models.Model):
    SEXO_CHOICES = (
        ('m', 'masc'),
        ('f', 'fem'),
    )
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, default='m')
    nome = models.CharField(max_length=255, null=False, blank=False)
    data_nascimento = models.DateField(null=True, blank=True)
    cpf = models.CharField(max_length=16, unique=True, null=False, blank=False)
    foto = models.ImageField(upload_to='fotos', null=True, blank=True)
    telefone = models.OneToOneField(Telefone, clank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome