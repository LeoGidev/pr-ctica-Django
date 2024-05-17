from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def hola_mundo(request):
    return render(request, 'hola_mundo.html')


