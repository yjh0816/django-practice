from django.shortcuts import render, redirect
from .models import Member
# from django.http.response import HttpResponse

# Create your views here.
def login(request):
    if request.method == 'POST':
        print(request.session)
        user_id = request.POST.get("user_id")
        password = request.POST.get("password")
        # member = Member.objects.get(user_id=user_id,password=password)
        # print(member)
        if Member.objects.filter(user_id=user_id).exists():
            member = Member.objects.get(user_id=user_id)

            if member.password == password:
                # print(f"login success{member}")

                request.session['user_pk'] = member.id
                request.session['user_id'] = member.user_id
                return redirect('/')

        # print("login failed")
    return render(request,'login.html')


# def regist(request):
#     if request.method == 'POST':
#         member = Member(
#             user_id = request.POST.get("user_id"),
#             password = request.POST.get("password"),
#         )
#         member.save()
#         return redirect('/') 

#     return render(request,'/')
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