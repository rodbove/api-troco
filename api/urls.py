from django.urls import path
from . import views

urlpatterns = [
	path('', views.index),
	path('coins/', views.coins.as_view()),
	path('troco_certo/', views.troco_certo.as_view())
]