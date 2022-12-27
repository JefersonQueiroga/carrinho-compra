from django.db import models

# Create your models here.
class Produto(models.Model):
    nome = models.CharField(max_length=140)
    preco = models.FloatField()
    
    def __init__(self, *args, **kwargs):
        super(Produto, self).__init__(*args, **kwargs)
        self.quantidade = 0

class Pedido(models.Model):
    valor = models.FloatField()
    produtos = models.ManyToManyField(Produto)