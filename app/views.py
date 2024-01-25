from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponse

def registration(request):
    ufo=UserForms()
    pfo=ProfileForms()
    d={'ufo':ufo,'pfo':pfo}


    if request.method=='POST' and request.FILES:
        ufd=UserForms(request.POST)
        pfd=ProfileForms(request.POST,request.FILES)
        if ufd.is_valid() and pfd.is_valid():
            MUFDO=ufd.save(commit=False)
            pw=ufd.cleaned_data['password']
            MUFDO.set_password(pw)
            MUFDO.save()
            MPFDO=pfd.save(commit=False)
            MPFDO.username=MUFDO
            MPFDO.save()
            return HttpResponse('Registration is Successfull')
        else:
            return HttpResponse('invalide your data')
    return render(request,'registrations.html',d)
