from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from forum.models import College, School, Module, QuestionPage, QuestionPost, UserProfile
from forum.forms import UserForm, UserProfileForm, QuestionPageForm, QuestionPostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout
from forum.models import QuestionPost


def index(request):
    QuestionPage_list = QuestionPage.objects.order_by('views')[:5]
    context_dict = {'QuestionPages': QuestionPage_list}
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


def colleges(request):
    college_list = College.objects.all()
    context_dict = {'colleges': college_list}
    return render(request, 'forum/colleges.html', context_dict)


def schools(request, college_name_slug):
    context_dict = {}

    try:
        college = College.objects.get(slug=college_name_slug)
        school_list = School.objects.filter(college=college)
        context_dict['schools'] = school_list
        context_dict['college'] = college

    except College.DoesNotExist:
        context_dict['schools'] = None
        context_dict['college'] = None

    return render(request, 'forum/schools.html', context_dict)


def modules(request, college_name_slug, school_name_slug):
    context_dict = {}

    try:
        college = College.objects.get(slug=college_name_slug)
        school = School.objects.get(slug=school_name_slug)
        module_list = Module.objects.filter(school=school)
        context_dict['modules'] = module_list
        context_dict['school'] = school
        context_dict['college'] = college

    except College.DoesNotExist:
        context_dict['modules'] = None
        context_dict['school'] = None
        context_dict['college'] = None

    return render(request, 'forum/modules.html', context_dict)


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


def create_question(request):
    if request.method == 'POST':
        # Attempt to grab information from the raw input data
        question_page_form = QuestionPageForm(data=request.POST)
        question_post_form = QuestionPostForm(data=request.POST)

        # If the two forms are valid
        if question_page_form.is_valid() and question_post_form.is_valid():
            # Save user data to database

            # Holds back the saving of the question_page
            # until question_post data integrity is confirmed
            question_page = question_page_form.save()
            question_post = question_post_form.save(commit=False)
            question_post.page = question_page

            # For later implementation if we want pics in posts
            # Did the user supply a post picture?
            # if 'picture' in request.FILES:
            #    profile.picture = request.FILES['picture']

            # Save the QuestionPost model instance
            question_post.save()
        else:
            # Invalid form(s): Print errors to console/log
            print(question_page_form.errors, question_post_form.errors)
    else:
        return render(request, 'forum/create_question.html', {})

    return render(request, 'forum/create_question.html',
                  {'question_page_form': question_page_form, 'question_post_form': question_post_form})

# Shows all of the questions
def show_questions_page(request, module_name_slug):
    context_dict = {}

    module = Module.objects.get(slug=module_name_slug)
    questions = QuestionPage.objects.filter(module=module)

    context_dict['questions'] = questions
    context_dict['module']=module_name_slug

    return render(request, 'forum/questions.html', context_dict)


# Show each individual question
def show_question_page(request, question_page_name_slug):
    context_dict = {}

    question_page = QuestionPage.objects.get(slug=question_page_name_slug)
    question_posts = QuestionPost.objects.filter(questionPage=question_page)

    context_dict['questionPosts'] = question_posts
    context_dict['questionPage'] = question_page

    return render(request, 'forum/questionPage.html', context_dict)
