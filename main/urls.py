from django.urls import path
from . import views

urlpatterns = [
    path('exam', views.exam, name='exam'),
    path('exchange', views.exchange, name='exchange'),
    path('calc', views.calc, name='calc'),
]


