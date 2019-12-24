from django.urls import path
from . import views

urlpatterns = [
	path('listar_moedas/', views.listar_moedas.as_view()),
	path('criar_moeda/', views.criar_moeda.as_view()),
	path('atualizar_moeda/', views.atualizar_moeda.as_view()),
	path('deletar_moeda/', views.deletar_moeda.as_view()),
	path('troco_certo/', views.troco_certo.as_view())
]