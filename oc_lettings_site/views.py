from django.shortcuts import render
from .settings import SECRET_KEY


def index(request):
    data = {}
    data["secret_key"] = SECRET_KEY
    return render(request, "index.html", context={"data": data})
