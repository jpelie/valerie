from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Mhome(request):
    return render(request, '../OURPYTHONPRO/pages/index.html', )


def qui (request):
    return render(request, '../OURPYTHONPRO/pages/Quisommes_nous.html', )

def balde(request):
    return render(request,'../OURPYTHONPRO/pages/contact.html',)

def valerie (request):
    return render(request,'../OURPYTHONPRO/pages/Accueil.html',)

def pedro (request):
    return render(request,'../OURPYTHONPRO/pages/cours.html',)