from django.shortcuts import render
from .models import BaseLiquor

# Create your views here.
def baseliquor(request):
    baseliquors = BaseLiquor.objects.all()
    return render(request, 'baseliquor.html', {
        'baseliquors': baseliquors,
    })

# def liquor_detail(request, pk):
#     baseliquors = BaseLiquor.objects.get(pk=pk)
#     return render(request, 'whisky.html', {
#         'baseliquors': baseliquors,
#     })