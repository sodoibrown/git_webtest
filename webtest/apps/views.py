# from django.http import HttpResponse
from django.shortcuts import render
from .models import fuser

# def index(request):
#     return render(request, 'apps/templates/apps/index.html')

def index(request):
    fuser_obj = fuser.objects.all()

    if request.method == "POST":
        print(request.POST)


    return render(request, 'apps/templates/apps/index.html',
    {'fuser_obj':fuser_obj})

