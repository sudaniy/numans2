from django.shortcuts import render
from django.http import HttpResponse
from .models import Slider, About, Service, Gallery, News, Team

# Create your views here.

def home(request): 
    abouts = About.objects.all()
    slides = Slider.objects.all()
    services = Service.objects.all()[:6]
    galls = Gallery.objects.all()[:8]
    news = News.objects.all()[:3]
    team = Team.objects.all()
    return render(request, 'index.html', {'abouts':abouts, 'slides':slides, 'services':services, 'galls':galls,
                                        'news':news, 'team':team})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')


def service(request):
    return render(request, 'service.html')


def project(request):
    return render(request, 'projects.html')


def news(request):
    return render(request, 'news.html')


def team(request):
    return render(request, 'team.html')