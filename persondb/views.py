from django.shortcuts import render
from persondb.models import Person
# Create your views here.

def persons(request,**Kwargs):

    my_persons = Person.obejcts.all()
    return render(request,persons.html,context=my_persons)

