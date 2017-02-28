from django.contrib import admin
from forum.models import Category, Question

admin.site.register(Category)
admin.site.register(Question)