from django.urls import path
from . import views

urlpatterns = [
    path('tabela/', views.index, name='tabela'),
]