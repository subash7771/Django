from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render


class newAddForm(forms.Form):
    find = forms.CharField(label="New Find")

# Create your views here.
def index (request):
    if "finds" not in request.session:
        request.session["finds"] = []

    return render(request, "finds/index.html", {
        "finds": request.session["finds"]
    })

def add(request):
    if request.method == "POST":
        form = newAddForm(request.POST)
        if form.is_valid():
            find = form.cleaned_data["find"]
            request.session["finds"] += [find]
            return HttpResponseRedirect(reverse("finds:index"))
        else:
            return render(request, "finds/add.html", {
                "form": form 
            })

    return render(request, "finds/add.html", {
        "form": newAddForm()
    })
