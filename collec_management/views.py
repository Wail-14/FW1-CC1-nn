from django.shortcuts import render
from collec_management.models import *


def about(request):
    return render(request, 'about.html') 

def collection(request, n):
        collection = Collec.objects.get(pk=n)
        return render(request, 'collection.html', {'collection': collection})

def colleclist(request):
    collecs = Collec.objects.all()
    context = {"all_collec":collecs}
    return render(request,"collec_list.html",context)