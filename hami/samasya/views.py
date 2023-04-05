from django.shortcuts import render
from .models import Samasya

# Create your views here.
def index(request):
    return render(request, "samasya/index.html",{
        "samasya": Samasya.objects.all()
    })