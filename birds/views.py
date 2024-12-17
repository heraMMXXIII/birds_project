from django.shortcuts import render
from django.shortcuts import render
from .models import Bird

def bird_list(request):
    birds = Bird.objects.all()
    return render(request, 'birds/bird_list.html', {'birds': birds})

# Create your views here.
