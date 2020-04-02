from __future__ import unicode_literals

from django.shortcuts import render, redirect

from .forms import DevForm
from .models import Dev

def index(request):
    context = {
        "available_devs": Dev.objects.all()
    }
    return render(request, 'index.html', context=context)

def signup(request):
    context = {
        "form": DevForm(request.POST or None)
    }

    if request.method == "POST" and context["form"].is_valid():
        context["form"].save()
        return redirect('/')
    
    return render(request, 'cadastro.html', context=context) 