from django.shortcuts import render, redirect
from django.http.response import JsonResponse
from .models import Product

# Create your views here.
def main(request):
    products = Product.objects.all().order_by('-id')
    # products = Product.objects.filter(title__contains='test')

    return render(request,'product.html', {'products': products})
    # products의 key값은 dict의 key
    # product.html 파일 즉, templates에서 쓸 변수를 전달하기 위함

def detail(request, pk):
    product = Product.objects.get(pk=pk)
    # if product.image:
    #     image_url = product.image.url
    # else:
    #     image_url = "/static/prod1.jpg"
    
    ret = {
        'title': product.title,
        'content': product.content,
        'price': product.price,
        'location': product.location,
        'image': "/static/prod1.jpg",
    }
    if product.image:
        ret['image'] = product.image.url

    # return JsonResponse({
    #     'title': product.title,
    #     'content': product.content,
    #     'price': product.price,
    #     'location': product.location,
    #     'image': image_url,
    # })

    return JsonResponse(ret)

def write(request):
    # print(request.method) # reload시 'GET' 출력
    if not request.session.get('user_id'):
        return redirect('/member/login/')
    if request.method == 'POST':
        # print(request.POST) # 입력한 내용을 dict로 반환
        product = Product(
            title = request.POST.get("title"),
            content = request.POST.get("content"),
            price = request.POST.get("price"),
            location = request.POST.get("location"),
            image = request.FILES.get("image")
        )
        product.save()
        # 원하는 주소로 redict가능 /는 home으로 보낸다는 의미
        return redirect('/') 
        # return redirect(f'/product/{product.id}') 


    return render(request,'product_write.html')