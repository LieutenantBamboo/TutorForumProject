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
