from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categoria(models.Model):
    TIPO_CHOICES = (
        ('R', 'Receita'),
        ('D', 'Despesas'),

    )
    nome = models.CharField(verbose_name='Nome', max_length=50)
    tipo = models.CharField(verbose_name='Tipo', max_length=1, choices=TIPO_CHOICES)
    descricao = models.TextField(verbose_name='Descrição', blank=True, null=True)
    usuario = models.ForeignKey(User, verbose_name='Usuario', on_delete=models.CASCADE)


    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['nome']


    def __str__(self):
        return self.nome

