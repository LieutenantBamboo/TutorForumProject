from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render, render_to_response
from django.contrib.auth import authenticate, login, logout
from forum.models import College, School, Module, QuestionPage, QuestionPost, UserProfile
from forum.forms import UserForm, UserProfileForm, QuestionPageForm, QuestionPostForm, CommentForm, UserGroupForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.template import RequestContext
from forum.models import QuestionPost, Comment
from django.contrib.postgres import *
from django.shortcuts import get_object_or_404

import uuid


def index(request):
    question_page_list = QuestionPage.objects.order_by('views')[:5]
    context_dict = {'question_pages': question_page_list}
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


def register(request):
    # Boolean whether registration was successful, false by default
    registered = False

    # If POST, process data
    if request.method == 'POST':
        # Attempt to grab information from the raw input data
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        group_form = UserGroupForm(data=request.POST)

        # If the two forms are valid
        if user_form.is_valid() and profile_form.is_valid() and group_form.is_valid():
            # Save user data to database
            user = user_form.save()

            # Hashes the user password and updates it with the save method
            user.set_password(user.password)
            user.save()

            # Holds back the saving of the profile model
            # until data integrity is confirmed
            profile = profile_form.save(commit=False)
            profile.user = user

            # Assigns group
            foobar = group_form.cleaned_data
            group = foobar.get('group')
            group.user_set.add(user)

            # Did the user supply a profile picture?
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # Save the UserProfile model instance
            profile.save()

            # Show the user registration was successful
            registered = True
        else:
            # Invalid form(s): Print errors to console/log
            print(user_form.errors, profile_form.errors, group_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
        group_form = UserGroupForm()

    # Render the template depending on the context
    return render(request, 'forum/register.html',
                  {'user_form': user_form, 'profile_form': profile_form, 'group_form': group_form,'registered': registered})


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
    next = ''

    if request.GET:
        next = request.GET.get('next')

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

                if next is not '':
                    return HttpResponseRedirect(next)
                else:
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
        # return render(request, 'forum/login.html', {})
        return render(request, 'forum/login.html', {'next': next, })


@login_required
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
            question_page = question_page_form.save(commit=True)
            question_post = question_post_form.save(commit=False)

            question_post.user = UserProfile.objects.get(user=request.user)
            question_post.pid = question_page.num_of_posts
            question_post.page = question_page
            question_post.question = True

            # For later implementation if we want pics in posts
            # Did the user supply a post picture?
            # if 'picture' in request.FILES:
            #    profile.picture = request.FILES['picture']

            # Save the QuestionPost model instance
            question_post.save()
            return HttpResponseRedirect(reverse('index'))
        else:
            # Invalid form(s): Print errors to console/log
            print(question_page_form.errors, question_post_form.errors)
    else:
        question_post_form = QuestionPostForm
        question_page_form = QuestionPageForm

    return render(request, 'forum/create_question.html',
                  {'question_page_form': question_page_form, 'question_post_form': question_post_form})


# Shows all of the questions
def show_questions_page(request, module_name_slug):
    context_dict = {}

    module = Module.objects.get(slug=module_name_slug)
    questions = QuestionPage.objects.filter(module=module)

    context_dict['questions'] = questions
    context_dict['module'] = module

    return render(request, 'forum/questions.html', context_dict)


# Show each individual question
def show_question_page(request, module_name_slug, question_page_name_slug):
    context_dict = {}

    module = Module.objects.get(slug=module_name_slug)
    question_page = QuestionPage.objects.get(slug=question_page_name_slug)
    question_posts = QuestionPost.objects.filter(page=question_page)
    comments = Comment.objects.filter(post__in=question_posts)
    comment_form = CommentForm
    post_form = QuestionPostForm
    is_tutor = request.user.groups.filter(name='Tutor').exists()

    context_dict['question_posts'] = question_posts
    context_dict['question_page'] = question_page
    context_dict['comments'] = comments
    context_dict['module'] = module
    context_dict['post_form'] = post_form
    context_dict['comment_form'] = comment_form
    context_dict['is_tutor'] = is_tutor

    return render(request, 'forum/questionPage.html', context_dict)


def create_post(request, module_name_slug, question_page_name_slug):
    context_dict = {}

    module = Module.objects.get(slug=module_name_slug)
    question_page = QuestionPage.objects.get(slug=question_page_name_slug)
    question_posts = QuestionPost.objects.filter(page=question_page)
    comments = Comment.objects.filter(post__in=question_posts)

    if request.method == 'POST':
        comment_form = CommentForm
        post_form = QuestionPostForm(data=request.POST)
        if post_form.is_valid():

            # Save comment instance
            post = post_form.save(commit=False)
            post.user = UserProfile.objects.get(user=request.user)
            post.pid = question_page.num_of_posts + 1
            question_page.num_of_posts += 1
            question_page.save()
            post.page = question_page
            post.save()

        else:
            # Invalid form(s): Print errors to console/log
            print(post_form.errors)
        post_form = QuestionPostForm
    else:
        post_form = QuestionPostForm
        comment_form = CommentForm

    context_dict['question_posts'] = question_posts
    context_dict['question_page'] = question_page
    context_dict['comments'] = comments
    context_dict['module'] = module
    context_dict['post_form'] = post_form
    context_dict['comment_form'] = comment_form

    return HttpResponseRedirect(
        '/forum/questions/%s/%s/' % (module.slug, question_page.slug))


def create_comment(request, module_name_slug, question_page_name_slug, question_post=None):
    context_dict = {}

    module = Module.objects.get(slug=module_name_slug)
    question_page = QuestionPage.objects.get(slug=question_page_name_slug)
    question_posts = QuestionPost.objects.filter(page=question_page)
    comments = Comment.objects.filter(post__in=question_posts)

    if request.method == 'POST':
        post_form = QuestionPostForm
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Save comment instance
            comment = comment_form.save(commit=False)
            q_post = question_post  # request.POST.get('question_post')
            comment.post = get_object_or_404(QuestionPost, pid=q_post)
            comment.user_profile = UserProfile.objects.get(user=request.user)
            comment.save()
        else:
            # Invalid form(s): Print errors to console/log
            print(comment_form.errors)
        comment_form = CommentForm
    else:
        comment_form = CommentForm
        post_form = QuestionPostForm

    context_dict['question_posts'] = question_posts
    context_dict['question_page'] = question_page
    context_dict['comments'] = comments
    context_dict['module'] = module
    context_dict['post_form'] = post_form
    context_dict['comment_form'] = comment_form

    return HttpResponseRedirect(
        '/forum/questions/%s/%s/' % (module.slug, question_page.slug))


def other_profile(request, user_profile):
    context_dict = {'user_profile': user_profile}
    return render(request, 'forum/other_user.html', context_dict)


def search(request):
    if request.method == 'GET':
        searchText = request.GET.get('search')
        answers = QuestionPage.objects.filter(title=searchText)
    else:
        answers = ''

    context_dict = {}
    context_dict['answers'] = answers

    return render(request, 'forum/search.html', context_dict)


def likeQuestionPost(request, question_page_slug, question_post):
    if question_page_slug:
        question_page = QuestionPage.objects.get(slug=question_page_slug)
        question_post = QuestionPost.objects.get(pid=question_post.pid)
        question_post.upvotes += 1
        question_post.save()

    return HttpResponseRedirect(
        'forum/questions/%s/%s/%s' % question_page.module.slug % question_page.slug % question_page.title)


def dislikeQuestionPost(request, question_page_slug, question_post):
    if question_page_slug:
        question_page = QuestionPage.objects.get(slug=question_page_slug)
        question_post = QuestionPost.objects.get(pid=question_post.pid)
        question_post.downvotes += 1
        question_post.save()

    return HttpResponseRedirect(
        'forum/questions/%s/%s/%s' % question_page.module.slug % question_page.slug % question_page.title)


def deleteQuestionPost(request, questionpage_slug):
    if questionpage_slug:
        question_page = QuestionPage.objects.get(slug=questionpage_slug)
        question_post = QuestionPost.objects.get(page=question_page)
        question_post.delete()

    return HttpResponseRedirect(reverse('index'))
