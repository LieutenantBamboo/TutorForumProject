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
    url(r'^questions/(?P<module_name_slug>[\w\-]+)/(?P<question_name_slug>[\w\-]+)/$', views.show_question_page, name='question'),

    # Miscellaneous urls
    url(r'^about/', views.about, name='about'),
    url(r'^contact_us/', views.contact_us, name='contact_us'),
    url(r'^hall_of_shame/', views.hallOfShame, name='hallOfShame'),
    url(r'^latest_news/', views.latestNews, name='latestNews'),
    url(r'^FAQ/', views.FAQ, name='FAQ'),
    url(r'^leisure/', views.leisure, name='leisure'),
    url(r'^register/', views.register, name='register'),
    url(r'^profile/', views.profile, name='profile'),
    # Login url setup
    url(r'^login/', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),

    # how to add a link to questionPage?? need to add module,
]
