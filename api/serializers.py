from rest_framework import serializers


class criar_moeda(serializers.Serializer):
	valor = serializers.FloatField()
	tipo = serializers.CharField(max_length=10)
	codigo = serializers.CharField(max_length=10)


class atualizar_moeda(serializers.Serializer):
	campo = serializers.CharField(max_length=10)


class deletar_moeda(serializers.Serializer):
	id = serializers.IntegerField()


class troco_certo(serializers.Serializer):
	valor_total = serializers.FloatField()
	valor_pago = serializers.FloatField()