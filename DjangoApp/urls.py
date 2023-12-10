from django.contrib import admin
from django.urls import path, include
from DjangoApp import views
from django.conf.urls.static import static
from django.conf import settings

app_name = "main"

urlpatterns = [
    path('', views.index, name='index'),
    path('settings', views.settings, name='settings'),
    path('upload', views.upload, name='upload'),
    path('follow', views.follow, name='follow'),
    path('profile/<str:pk>', views.profile, name='profile'),
    path('signup', views.signup, name='signup'),
    path('upload', views.upload, name='upload'),
    path('search', views.search, name='search'),
    path('signin', views.signin, name='signin'),
    path('terms', views.terms, name='terms'),
    path('like-post', views.like_post, name='like-post'),
    path('logout', views.logout, name='logout'),
    path('admin/', admin.site.urls),
]

