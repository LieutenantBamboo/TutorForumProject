from django.contrib import admin
from forum.models import College, School, Module, QuestionPage, UserProfile, Comment, QuestionPost,upvoteQuestionPost,downvoteQuestionPost



admin.site.register(College)
admin.site.register(School)
admin.site.register(Module)
admin.site.register(QuestionPage)
admin.site.register(UserProfile)
admin.site.register(Comment)
admin.site.register(QuestionPost)
admin.site.register(upvoteQuestionPost)
admin.site.register(downvoteQuestionPost)
