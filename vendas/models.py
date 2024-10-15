from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal

# Modelo para Frutas
class Fruta(models.Model):
    CLASSIFICACAO_CHOICES = [
        ('EX', 'Extra'),
        ('1', 'De Primeira'),
        ('2', 'De Segunda'),
        ('3', 'De Terceira'),
    ]

    nome = models.CharField(max_length=100)
    classificacao = models.CharField(max_length=2, choices=CLASSIFICACAO_CHOICES)
    fresca = models.BooleanField(default=True)
    quantidade = models.PositiveIntegerField(null=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome

# Modelo para Vendas
class Venda(models.Model):
    fruta = models.ForeignKey(Fruta, on_delete=models.CASCADE)
    quantidade = models.IntegerField(null=True)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    desconto = models.DecimalField(max_digits=5, decimal_places=2)
    vendedor = models.ForeignKey(User, on_delete=models.CASCADE)
    horario = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.quantidade} de {self.fruta.nome} vendidos por {self.vendedor.username}'

    @property
    def valor_com_desconto(self):
        return self.valor_total * (1 - self.desconto / 100)
