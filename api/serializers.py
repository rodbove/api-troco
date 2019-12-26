from rest_framework import serializers

class listar_moedas(serializers.Serializer):
	codigo = serializers.CharField(max_length=10)
	

class criar_moeda(serializers.Serializer):
	valor = serializers.FloatField()
	tipo = serializers.CharField(max_length=10)
	codigo = serializers.CharField(max_length=10)


class atualizar_moeda(serializers.Serializer):
	moeda_id = serializers.IntegerField()
	novo_valor = serializers.IntegerField()


class deletar_moeda(serializers.Serializer):
	moeda_id = serializers.IntegerField()


class troco_certo(serializers.Serializer):
	valor_total = serializers.FloatField()
	valor_pago = serializers.FloatField()
