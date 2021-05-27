from django.shortcuts import render
from .models import Person
# Create your views here.


def index(request):
    return render(request,'index.html',{})

def persons(request):
    my_persons = Person.objects.all()
    return render(request,'persons.html',{'my_persons':my_persons})

