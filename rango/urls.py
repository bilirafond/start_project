"""tango_with_django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from . import views


app_name = 'rango'

urlpatterns = [
    path('about/', views.about, name='about'),
    path('', views.index, name='index'),
    path('category/<category_name_slug>/', views.show_category, name='show_category'),
    path('add_category/', views.add_category, name='add_category'),
    path('<category_name_slug>/add_page/', views.add_page, name='add_page'),
]