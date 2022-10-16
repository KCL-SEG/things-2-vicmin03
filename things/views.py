from .forms import ThingsForm
from django.shortcuts import render

def home(request):
    form = ThingsForm()
    return render(request, 'home.html', {'form': form})
