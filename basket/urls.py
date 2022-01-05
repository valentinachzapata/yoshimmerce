from django.urls import path
from basket import views

app_name = 'basket'

urlpatterns = [
    path('', views.carrito_summary, name="carrito_summary"),
    path('add/', views.carrito_add, name="carrito_add"),
]
