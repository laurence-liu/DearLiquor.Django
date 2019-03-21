from django.shortcuts import render
from .models import BaseLiquor

# Create your views here.
def baseliquor(request):
    baseliquors = BaseLiquor.objects.all()
    return render(request, 'baseliquor.html', {
        'baseliquors': baseliquors,
    })

def whisky(request):
    return render(request, 'whisky.html', {})