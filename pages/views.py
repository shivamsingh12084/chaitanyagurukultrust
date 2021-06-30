from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *

# Create your views here.
def HomePageView(request):
    images = News.objects.all()
    context = {'images':images}
    return render(request, 'home.html', context)

class AboutPageView(TemplateView):
    template_name = 'about.html'

def Admission(request):
    context = {}
    return render(request, 'admission.html', context)

def Acadimics(request):
    context = {}
    return render(request, 'academics.html', context )


def Alumni(request):
    context = {}
    return render(request, 'alumni.html', context )
     

def Career(request):
    context = {}
    return render(request, 'career.html', context)


def CgtOverview(request):
    context = {}
    return render(request, 'cgtOverview.html', context )

def ChaitanyaMeaning(request):
    context = {}
    return render(request, 'chaitanyaMeaning.html', context)


def CoCurricular(request):
    context = {}
    return render(request, 'coCurricular.html', context)

def Mentors(request):
    context = {}
    return render(request, 'mentors.html', context)

def Boards(request):
    context = {}
    return render(request, 'board.html', context)


def SocialService(request):
    context = {}
    return render(request, 'socialservice.html', context)

def Trips(request):
    context = {}
    return render(request, 'trips.html', context)


def Vission(request):
    context = {}
    return render(request, 'vission.html', context)


def Physical(request):
    context = {}
    return render(request, 'physical.html', context)