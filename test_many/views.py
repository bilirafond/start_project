from django.shortcuts import render
from .forms import RegistrationForm

# Create your views here.


def registration(request):
    return render(request, 'registration.html', {'form': RegistrationForm})
