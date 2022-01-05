from django.shortcuts import get_object_or_404, render
from .models import Category, Product

def all_products(request):
    products = Product.objects.all()
    return render(request, 'home.html', { 'products' : products })

def detail_products(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'detail.html', { 'product' : product })

def list_category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'category.html', { 'category' : category, 'products' : products})