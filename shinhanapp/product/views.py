from django.shortcuts import render
from django.http.response import JsonResponse
from .models import Product

# Create your views here.
def main(request):
    products = Product.objects.all()
    # products = Product.objects.filter(title__contains='test')

    return render(request,'product.html', {'products': products})

def detail(request, pk):
    product = Product.objects.get(pk=pk)

    return JsonResponse({
        'title': product.title,
        'content': product.content,
        'price': product.price,
        'location': product.location,
    })

def writepage(request):
    return render(request,'write.html')