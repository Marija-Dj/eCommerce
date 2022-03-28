from django.shortcuts import render, get_object_or_404

from .models import Category, Product

def categories(raquest):
    return {
        'categories':Category.objects.all()
    }

def all_products(request):
    products = Product.objects.all()
    return render (request, 'product/index.html', {'products':products})


def detail_product(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'product/detail.html', {'product': product})

def category_list(request, category_slug):
    catrgory = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(catrgory=catrgory)
    return render(request, 'product/category.html', {'category': catrgory, 'products': products})


