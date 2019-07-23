"""cultdevcow URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.urls import include

from core import views

urlpatterns = [
    path('index/', views.index),
    path('admin/', admin.site.urls),
    url(r'^routing/', include('routing.urls')),
    url(r'^template/', include('template.urls')),

    # url(r'^routing/',
    #     include([
    #         url(r'simple_route/$', views.simple_route),
    #         url(r'slug_route/(?P<slug>[\w\-]{1,16})/$', views.slug_route),
    #         url(r'sum_route/(?P<n>\-?\d+)/(?P<m>\-?\d+)/$', views.sum_route),
    #         url(r'sum_get_method/$', views.sum_get_method),
    #         # url(r'sum_get_method/\?a=\-?\d+\&b=\-?\d+$', views.sum_get_method),
    #         url(r'sum_post_method/$', views.sum_post_method),
    #     ])),
    #
    # url(r'^echo/$', views.echo),
    # url(r'^filters/$', views.filters),
    # url(r'^extend/$', views.extend),
]
