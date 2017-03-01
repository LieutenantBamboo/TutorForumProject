from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render
from forum.models import Category, Question


def index(request):
    category_list = Category.objects.order_by('name')
    context_dict = {'categories': category_list}
    return render(request, 'forum/index.html', context_dict)


def about(request):
    context_dict = {}
    return render(request, 'forum/about.html', context_dict)


# Later to be repurposed if the site produces multiples apps
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

# def show_category(request, category_name_slug):
#	context_dict={}
#	try:
#		category=Category.objects.get(slug=category_name_slug)
#		questions=Question.objects.filter(category=category)
#		
#		context_dict['questions']=questions
#		context_dict['category']=category
#	
#	except Category.DoesNotExist
#		context_dict['category'] = None
#		context_dict['pages'] = None
#	
#	return render(request, 'forum/show_categories.html', context_dict)
