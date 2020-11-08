from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework	import status

from django.shortcuts import render, redirect
from .models import moedaCorrente
from . import serializers

from collections import Counter

# Página inicial
def index(request):
	return render(request, 'api/index.html')

	
class coins(APIView):
	def get(self, request, format=None):
		"""Recebe o código desejadoRetorna uma lista com valores, tipo e código das moedas disponívels na base."""

		serializer = serializers.listar_moedas(data=request.query_params)
		print(serializer)

		moedas = []

		if serializer.is_valid():
			codigo = serializer.data.get('codigo')		
			for m in moedaCorrente.objects.filter(codigo=codigo):
				moedas.append(f'id: {m.id}, R${m.valor}, Tipo: {m.tipo}, Código: {m.codigo}')
			return Response({'moedas': moedas})
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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

	def put(self, request):
		"""Atualiza um objeto específico na base"""

		serializer = serializers.atualizar_moeda(data=request.data)

		if serializer.is_valid():
			moeda_id = serializer.data.get('moeda_id')
			novo_valor = serializer.data.get('novo_valor')
			moeda = moedaCorrente.objects.get(id=moeda_id)

			moeda.valor = novo_valor
			moeda.save()
			
			return Response({'message': f'Moeda com id {moeda.id} recebeu novo valor.'})
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk=None):
		"""Deleta um objeto na base utilizando pesquisa por id"""

		serializer = serializers.deletar_moeda(data=request.query_params)

		if serializer.is_valid():
			objeto = moedaCorrente.objects.get(id=serializer.data.get('moeda_id'))
			objeto.delete()
			return Response({'message': f"Moeda de id '{serializer.data.get('moeda_id')}' deletada com sucesso."})
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
					 
			# Confere se o valor dado pelo cliente supre o valor da compra
			if valor_pago < valor_total:
				return Response(f'Valor recebido é menor do que o total da compra, faltam R${valor_total - valor_pago} para finalizar a compra.')
			else:
				troco_total = valor_pago - valor_total
				zerar_troco = troco_total
				devolver = []
				
				# Lógica para descobrir quais notas serão utilizadas para devolver o troco correto
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

				return Response(f'Troco total: {troco_total}. Devolver com as seguintes notas e moedas: {display}')


		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

