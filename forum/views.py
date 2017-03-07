from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from forum.models import College, School, Module, QuestionPage, QuestionPost, UserProfile
from forum.forms import UserForm, UserProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout


def index(request):
    college_list = College.objects.order_by('name')
    context_dict = {'categories': college_list}
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


def FAQ(request):
    context_dict = {}
    return render(request, 'forum/FAQ.html', context_dict)


def leisure(request):
    context_dict = {}
    return render(request, 'forum/leisure.html', context_dict)


def register(request):
    # Boolean whether registration was successful, false by default
    registered = False

    # If POST, process data
    if request.method == 'POST':
        # Attempt to grab information from the raw input data
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid
        if user_form.is_valid() and profile_form.is_valid():
            # Save user data to database
            user = user_form.save()

            # Hashes the user password and updates it with the save method
            user.set_password(user.password)
            user.save()

            # Holds back the saving of the profile model
            # until data integrity is confirmed
            profile = profile_form.save(commit=False)
            profile.user = user

            # Did the user supply a profile picture?
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # Save the UserProfile model instance
            profile.save()

            # Show the user registration was successful
            registered = True
        else:
            # Invalid form(s): Print errors to console/log
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context
    return render(request, 'forum/register.html',
                  {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})


@login_required
def profile(request):
    context_dict = {}
    return render(request, 'forum/profile.html', context_dict)


@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)
    # Take the user back to the homepage.
    return HttpResponseRedirect(reverse('index'))


def user_login(request):
    if request.method == 'POST':
        # Requests information using getter
        # methods that return 'None' if no info
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticates information
        user = authenticate(username=username, password=password)

        # If correctly authenticated
        if user:

            # If active
            if user.is_active:
                # Logs user in, sends back to homepage
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                # Warns the user that their account is inactive
                return HttpResponse("Your account is disabled. Please contact the admins")
        else:
            # Bad login details
            print("Bad login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied")

    # If not POST (positng details), then it's GET, therefore login form is displayed
    else:
        return render(request, 'forum/login.html', {})

# def show_category(request, category_name_slug):
# context_dict={}
# try:
# 	category=Category.objects.get(slug=category_name_slug)
# 	questions=Question.objects.filter(category=category)
#
# 	context_dict['questions']=questions
# 	context_dict['category']=category
#
# except Category.DoesNotExist
# 	context_dict['category'] = None
# 	context_dict['pages'] = None
#
# return render(request, 'forum/show_categories.html', context_dict)
