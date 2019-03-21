from django.shortcuts import render
from .models import Cocktail

# Create your views here.
def cocktail(request):
    cocktails = Cocktail.objects.all()
    return render(request, 'cocktail.html', {
        'cocktails': cocktails,
    })