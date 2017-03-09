from django.contrib import admin
from forum.models import College, School, Module, QuestionPage, UserProfile, Comment, QuestionPost


class QuestionPageAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('title',)}




admin.site.register(College)
admin.site.register(School)
admin.site.register(Module)
admin.site.register(QuestionPage, QuestionPageAdmin)
admin.site.register(UserProfile)
admin.site.register(Comment)
admin.site.register(QuestionPost)
