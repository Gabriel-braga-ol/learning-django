from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    print('HOME')

    context = {
        'text': 'Olá home',
        'title': 'Página home - '
    }

    return render(
        request,
        'home/index.html',
        context,
    )

