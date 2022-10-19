from django.shortcuts import render
from .settings import SECRET_KEY


def index(request):
    return render(request, "index.html")
