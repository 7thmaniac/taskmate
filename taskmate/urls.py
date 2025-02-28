"""
URL configuration for taskmate project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from todolist_app import views as todolist_app_views
from users_app import views as users_app_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('task/', include('todolist_app.urls')),
    path('user_account/', include('users_app.urls')),
    path('', todolist_app_views.index, name='index'),
    path('contact_us/', todolist_app_views.contact_us, name='contact_us'),
    path('about_us/', todolist_app_views.about_us, name='about_us'),
]
