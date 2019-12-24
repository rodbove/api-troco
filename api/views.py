from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework	import status

from django.shortcuts import render, redirect
from .models import moedaCorrente
from . import serializers

from collections import Counter

	
class listar_moedas(APIView):
	def get(self, request, format=None):
		"""Retorna uma lista com valores, tipo e código das moedas disponívels na base."""

		moedas = []

		for m in moedaCorrente.objects.all():
			moedas.append(f'id: {m.id}, R${m.valor}, Tipo: {m.tipo}, Código: {m.codigo}')

		return Response({'message': 'Moedas atualmente no sistema', 'moedas': moedas})


class criar_moeda(APIView):
	def post(self, request): 
		"""Cria uma nova moeda com valor, tipo e código na base."""

		serializer = serializers.criar_moeda(data=request.data)

		if serializer.is_valid():
			nova_moeda = moedaCorrente(valor=serializer.data.get('valor'), tipo=serializer.data.get('tipo'), codigo=serializer.data.get('codigo'))
			nova_moeda.save()
			message = 'Nova moeda registrada com sucesso.'
			return Response({'message': message})
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class atualizar_moeda(APIView):
	def put(self, request, pk=None):
		"""Atualiza um objeto específico na base"""

		serializer = serializers.atualizar_moeda(data=request.data)

		if serializer.is_valid():
			campo = serializer.data.get('campo')

		return Reponse({'method': 'put'})


class deletar_moeda(APIView):
	def delete(self, request, pk=None):
		"""Deleta um objeto na base utilizando pesquisa por id"""

		serializer = serializers.deletar_moeda(data=request.data)

		if serializer.is_valid():
			objeto = moedaCorrente.objects.get(id=serializer.data.get('id'))
			objeto.delete()
			message = 'Moeda deletada da base'
			return Response({'message': message})
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class troco_certo(APIView):
	def post(self, request):
		"""Recebe o valor_total da compra e o valor_pago pelo cliente.
		   Retorna o troco total e as cédulas a serem devolvidas na menor quantidade possível."""

		moedas = moedaCorrente.objects.all()
		valores = []

		for moeda in moedas:
			valores.append(moeda.valor)

		serializer = serializers.troco_certo(data=request.data)

		if serializer.is_valid():
			valor_total = serializer.data.get('valor_total')
			valor_pago = serializer.data.get('valor_pago')

			if valor_pago < valor_total:
				return Response(f'Valor recebido é menor do que o total da compra, faltam R${valor_total - valor_pago} para finalizar a compra.')
			else:
				troco_total = valor_pago - valor_total
				zerar_troco = troco_total
				devolver = []

				while zerar_troco > 0:
					for i in valores:
						if i <= zerar_troco:
							while i <= zerar_troco:
								zerar_troco -= i
								devolver.append(i)

				c = Counter(devolver)
				display = []

				for key in c:
					display.append(f'{c[key]}x R${key}')

				return Response(f'Troco total: {troco_total}. Devolver com as seguintes notas: {display}')


		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

