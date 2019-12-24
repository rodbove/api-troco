from djongo import models

class moedaCorrente(models.Model):
	valor = models.FloatField()
	tipo = models.CharField(max_length=5)
	codigo = models.CharField(max_length=5, default='BRL')

	def __str__(self):
		return str(self.valor)

# class transacoes(models.Model):
# 	valorTotal = models.DecimalField(max_digits=8, decimal_places=2)
# 	valorPago = models.DecimalField(max_digits=8, decimal_places=2)
#   criada_em = models.DateTimeField('date published')
# 	