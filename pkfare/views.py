from django.shortcuts import render
from pkfare import Mymodelform
from django.shortcuts import Http404


# Create your views here.
def index(request):
    form = Mymodelform.AirLegsList()
    return render(request, "index.html", {"form": form})
