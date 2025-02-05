from django.db import models

class Produto(models.Model):
    imagem = models.URLField()
    nome = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    parcelamento = models.CharField(max_length=100, null=True, blank=True)
    link = models.URLField()
    preco_sem_desconto = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    percentual_desconto = models.CharField(max_length=10, null=True, blank=True)
    tipo_entrega = models.CharField(max_length=10)
    frete_gratis = models.BooleanField()

    def __str__(self):
        return self.nome
