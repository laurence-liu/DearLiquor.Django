from django.shortcuts import render
# from django.apps import apps
from baseliquor.models import BaseLiquor

# Create your views here.
def store(request):
    # baseliquors = apps.get_model('baseliquor', 'BaseLiquor').objects.all()
    baseliquors = BaseLiquor.objects.all()
    return render(request, 'store.html', {
        'baseliquors': baseliquors,
    })