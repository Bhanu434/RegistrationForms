from django.shortcuts import render

# Create your views here.
from app.forms import *

def registration(request):
    ufo=UserForms()
    pfo=ProfileForms()
    d={'ufo':ufo,'pfo':pfo}
    return render(request,'registrations.html',d)
