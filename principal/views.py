from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
# Create your views here.
def Mhome(request):
    t = get_template('OURPYTHONPRO/pages/index.html')
    return render(request, t )


def qui (request):
    return render(request, '../OURPYTHONPRO/pages/Quisommes_nous.html', )

def balde(request):
    return render(request,'../OURPYTHONPRO/pages/contact.html',)

def valerie (request):
    return render(request,'../OURPYTHONPRO/pages/Accueil.html',)

def pedro (request):
    return render(request,'../OURPYTHONPRO/pages/cours.html',)