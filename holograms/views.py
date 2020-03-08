from django.shortcuts import render
from .forms import ClientForm
from .models import Client
from django.http import HttpResponse
import django
from django.conf import settings
from django.core.mail import send_mail

def holograms(request):
    if request.method == "POST":
        form = ClientForm(data=request.POST)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            phone = form.cleaned_data.get("phone")
            print(name)
            print(phone)
            data = "Имя=" + name + "\nТелефон=" + phone
            if name and phone:
                send_mail(subject='Новый заказ!', message=data, from_email="holoray@yandex.ru", recipient_list=["holoray@yandex.ru"], fail_silently=False)
            return render(request, 'holograms/alert.html', {})
        else:
            return render(request, 'holograms/index.html', {})
    else:
        form = ClientForm()
    return render(request, 'holograms/index.html', {})

def alert(request):
    return render(request, 'holograms/alert.html', {})

def fa30n(request):
    return render(request, 'holograms/fa30n.html', {})

def fa42hd(request):
    return render(request, 'holograms/fa42hd.html', {})

def fa65n(request):
    return render(request, 'holograms/fa65n.html', {})

def fa70n(request):
    return render(request, 'holograms/fa70n.html', {})

def fa85n(request):
    return render(request, 'holograms/fa85n.html', {})

def fa100n(request):
    return render(request, 'holograms/fa100n.html', {})

def gobo20(request):
    return render(request, 'holograms/gobo20.html', {})

def gobo30(request):
    return render(request, 'holograms/gobo30.html', {})

def gobo50(request):
    return render(request, 'holograms/gobo50.html', {})

def gobo80(request):
    return render(request, 'holograms/gobo80.html', {})