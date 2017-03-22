from django import forms
from forum.models import UserProfile, QuestionPage, QuestionPost
from django.contrib.auth.models import User
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


class QuestionPageForm(forms.ModelForm):
    # module = forms.ModelChoiceField(queryset=Module.objects.all().order_by('name'))

    class Meta:
        model = QuestionPage
        fields = ('title',)  # 'module',)


class QuestionPostForm(forms.ModelForm):
    class Meta:
        model = QuestionPost
        fields = ('text_field',)
