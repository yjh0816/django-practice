from django.shortcuts import render
from .models import Member
# from django.http.response import HttpResponse

# Create your views here.
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