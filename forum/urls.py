from django.conf.urls import url
from forum import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^contact_us/', views.contact_us, name='contact_us'),
    url(r'^categories/', views.categories, name='categories'),
    url(r'^hall_of_shame/', views.hallOfShame, name='hallOfShame'),
    url(r'^latest_news/', views.latestNews, name='latestNews'),
    url(r'^login/', views.login, name='login'),
    url(r'^FAQ/', views.FAQ, name='FAQ'),
    url(r'^leisure/', views.leisure, name='leisure'),
]
