from django.shortcuts import render

def holograms(request):
    return render(request, 'holograms/index.html', {})

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