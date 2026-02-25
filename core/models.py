from django.db import models

# Create your models here.
class Livro(models.Model):

    TIPO_CHOICES = [
        ('quero', 'Quero Ler'),
        ('lido', 'Lido'),
        ('comprado', 'Comprado'),
    ]

    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    ano = models.CharField(max_length=10, blank=True)
    paginas = models.IntegerField(default=0)
    categoria = models.CharField(max_length=100, blank=True)
    capa = models.URLField(blank=True)

    tipo = models.CharField(
        max_length=10,
        choices = TIPO_CHOICES
    )

    def __str__(self):

        return self.titulo


