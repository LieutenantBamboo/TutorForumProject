from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render


def index(request):
    context_dict = {}
    return render(request, 'forum/index.html', context_dict)


def about(request):
    context_dict = {}
    return render(request, 'forum/about.html', context_dict)

def home(request):
    return HttpResponseRedirect(reverse('index'))

	
def contact_us(request):
    context_dict = {}
    return render(request, 'forum/contact_us.html', context_dict)
	
def categories(request):
    context_dict = {}
    return render(request, 'forum/categories.html', context_dict)

def hallOfShame(request):
    context_dict = {}
    return render(request, 'forum/hallOfShame.html', context_dict)

def latestNews(request):
    context_dict = {}
    return render(request, 'forum/latestNews.html', context_dict)

def login(request):
    context_dict = {}
    return render(request, 'forum/login.html', context_dict)

def FAQ(request):
    context_dict = {}
    return render(request, 'forum/FAQ.html', context_dict)

def leisure(request):
    context_dict = {}
    return render(request, 'forum/leisure.html', context_dict)




