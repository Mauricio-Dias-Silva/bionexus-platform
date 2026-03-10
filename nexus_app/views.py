from django.shortcuts import render

def nexus_index(request):
    return render(request, 'nexus_app/index.html')

def transcendence(request):
    return render(request, 'nexus_app/transcendence.html')

def bioelectric(request):
    return render(request, 'nexus_app/bioelectric.html')

def touchless(request):
    return render(request, 'nexus_app/touchless.html')

def biomimicry(request):
    return render(request, 'nexus_app/biomimicry.html')
