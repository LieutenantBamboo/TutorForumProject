from django.conf.urls import url
from forum import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^contact_us/', views.contact_us, name='contact_us'),
    url(r'^colleges/', views.colleges, name='colleges'),
    url(r'^hall_of_shame/', views.hallOfShame, name='hallOfShame'),
    url(r'^latest_news/', views.latestNews, name='latestNews'),
    url(r'^login/', views.user_login, name='login'),
    url(r'^FAQ/', views.FAQ, name='FAQ'),
    url(r'^leisure/', views.leisure, name='leisure'),
    url(r'^register/', views.register, name='register'),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^logout/$', views.user_logout, name='logout'),

    #how to add a link to questionPage?? need to add module,
]
