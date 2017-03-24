from django.conf.urls import url
from forum import views

urlpatterns = [
    # Default url
    url(r'^$', views.index, name='index'),

    # Hierarchy url setup
    # College url
    url(r'^colleges/$', views.colleges, name='colleges'),
    # School url
    url(r'^colleges/(?P<college_name_slug>[\w\-]+)/$',
        views.schools, name='schools'),
    # Module url
    url(r'^colleges/(?P<college_name_slug>[\w\-]+)/(?P<school_name_slug>[\w\-]+)/$',
        views.modules, name='modules'),

    # Question url setup
    url(r'^questions/create/', views.create_question, name='create_question'),
    url(r'^questions/$', views.index, name='redirect'),
    url(r'^questions/(?P<module_name_slug>[\w\-]+)/$', views.show_questions_page, name='questions'),
    url(r'^questions/(?P<module_name_slug>[\w\-]+)/(?P<question_page_name_slug>[\w\-]+)/$',
        views.show_question_page, name='question'),
    url(
        r'^questions/(?P<module_name_slug>[\w\-]+)/(?P<question_page_name_slug>[\w\-]+)/(?P<question_post>\d+)',
        views.show_question_page, name='create-comment'),
    url(r'^questions/(?P<module_name_slug>[\w\-]+)/(?P<question_page_name_slug>[\w\-]+)/create',
        views.create_post, name='create-post'),

    # Miscellaneous urls
    url(r'^about/', views.about, name='about'),
    url(r'^contact_us/', views.contact_us, name='contact_us'),
    url(r'^hall_of_shame/', views.hallOfShame, name='hallOfShame'),
    url(r'^latest_news/', views.latestNews, name='latestNews'),
    url(r'^FAQ/', views.FAQ, name='FAQ'),
    url(r'^register/', views.register, name='register'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^profile/(?P<user_profile>[\w\-]+)/$', views.other_profile, name='other_profile'),
    # Login url setup
    url(r'^login/', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^search/$', views.search, name='search'),
    url(r'^questionPost/upvote/(?P<questionpage_slug>[\w\-]+)/$', views.likeQuestionPost, name='likeQuestionPost'),
    url(r'^questionPost/downvote/(?P<questionpage_slug>[\w\-]+)/$', views.dislikeQuestionPost, name='dislikeQuestionPost'),
    url(r'^questionPost/delete/(?P<questionpage_slug>[\w\-]+)/$', views.deleteQuestionPost, name='deleteQuestionPost'),


]
