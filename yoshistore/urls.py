from django.urls import path
from yoshistore import views

app_name = 'yoshistore'

urlpatterns = [
    path('', views.all_products, name = 'all_products'),
    path('<slug:slug>/', views.detail_products, name='detail_product'),
    path('search/<slug:category_slug>', views.list_category, name='list_category'),
]
