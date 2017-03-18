from django import forms
from forum.models import UserProfile, QuestionPage, QuestionPost
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture',)


class QuestionPageForm(forms.ModelForm):
    class Meta:
        model = QuestionPage
        fields = ('title',)

class QuestionPostForm(forms.ModelForm):
    text_field = forms.CharField(max_length=128,help_text = "Please enter the title of the page.")
    class Meta:
        model = QuestionPost
        fields = ('text_field', )