from django.shortcuts import render

def holograms(request):
    return render(request, 'holograms/index.html', {})
