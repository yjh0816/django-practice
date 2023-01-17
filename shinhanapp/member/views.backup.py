from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password, make_password
from .models import Member
# from django.http.response import HttpResponse

# Create your views here.
def login(request):
    if request.method == 'POST':
        print(request.session)
        user_id = request.POST.get("user_id")
        password = request.POST.get("password")

        if Member.objects.filter(user_id=user_id).exists():
            member = Member.objects.get(user_id=user_id)

            if check_password(password, member.password):
                request.session['user_pk'] = member.id
                request.session['user_id'] = member.user_id
                return redirect('/')

    return render(request,'login.html')

def logout(request):
    if 'user_pk' in request.session:
        del(request.session['user_pk'] )
    if 'user_id' in request.session:
        del(request.session['user_id'])

    return redirect('/')
def register(request):
    if request.method == 'POST':
        password = request.POST.get("password")
        user_id = request.POST.get("user_id")
        name = request.POST.get("name")
        age = request.POST.get("age")
       
        if not Member.objects.filter(user_id=user_id).exists():
            member = Member(
                user_id = user_id,
                password = make_password(password),
                name = name,
                age = age
            )
            member.save()
            return redirect('/member/login/') 

    return render(request,'register.html')
'''
def main(request):
    # return HttpResponse("Hello!")
    
    # member = Member()
    # member.name = 'test'
    # member.age = 20
    # member.save()

    # members = Member.objects.all()

    members = Member.objects.filter(name='test')

    # __str__의 역할
    # a = str(members[0])

    return render(request,'index.html', {'members': members})
'''