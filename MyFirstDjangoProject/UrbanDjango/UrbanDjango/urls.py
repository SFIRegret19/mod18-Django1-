"""
URL configuration for UrbanDjango project.

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
from django.urls import path
# from task2.views import view1, view2
# from example1.views import index
from task4.views import base, platform_page_index, catalog_page_index, cart_page_index
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('platform/', platform_page_index),
    path('platform/games/', catalog_page_index),
    path('platform/cart/', cart_page_index),
    path('base/', base)
    # path('index/', TemplateView.as_view(template_name='index2.html'))
]
