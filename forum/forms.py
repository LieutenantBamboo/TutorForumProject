from django import forms
from forum.models import UserProfile, QuestionPage, QuestionPost, Comment
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from forum.models import Module


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture',)


class UserGroupForm(forms.Form):
    group = forms.ModelChoiceField(queryset=Group.objects.all())

    class Meta:
        fields = ('group',)


class QuestionPageForm(forms.ModelForm):
    module = forms.ModelChoiceField(queryset=Module.objects.all().order_by('name'))

    class Meta:
        model = QuestionPage
        fields = ('title', 'module',)


class QuestionPostForm(forms.ModelForm):
    class Meta:
        model = QuestionPost
        fields = ('text_field',)


class CommentForm(forms.ModelForm):
    password = forms.CharField(label='Comment')

    class Meta:
        model = Comment
        fields = ('content',)
