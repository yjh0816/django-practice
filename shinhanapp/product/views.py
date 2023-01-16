from django.shortcuts import render
from .models import Product

# Create your views here.
def main(request):
    products = Product.objects.all()
    # products = Product.objects.filter(title__contains='test')

    return render(request,'product.html', {'products': products})
