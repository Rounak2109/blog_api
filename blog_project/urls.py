"""blog_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('thankyou/', TemplateView.as_view(template_name='thankyou.html'), name='thankyou'),
    path('email_sent/', TemplateView.as_view(template_name='email_sent.html'), name='email_sent'),
    path('admin/', admin.site.urls),
    path('posts/api/v1/', include('posts.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/rest-auth/', include('rest_auth.urls')),
    path('api/v1/rest-auth/registration/', include('rest_auth.registration.urls')),
    path('accounts/',include('allauth.urls')),
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
    # you CANNOT have this with the others...so i'm commenting it out as a reminder 
        # it will give this error: duplicate key value violates unique constraint "users_customuser_username_key" DETAIL:  Key (username)=() already exists.
    # path('accounts/', include('allauth.urls')),
]
