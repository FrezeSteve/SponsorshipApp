"""mysite URL Configuration

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
from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views
from scholarship.views import (index, scholarshipview, success, error, list_scholarship,
                               detail_scholarship, successfully, approve, list_scholarship_for_sponsors,
                                detail_scholarship_for_sponsors, approvesp
                               )
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('form/', scholarshipview, name='form'),
    path('success/', success, name='success'),
    path('error/', error, name='error'),
    path('list/', list_scholarship, name='list'),
    path('listsp/', list_scholarship_for_sponsors, name='listsp'),
    path('successfully/', successfully, name='successfully'),
    path('approve/<int:pk>/', approve, name='approve'),
    path('approvesp/<int:pk>/', approvesp, name='approvesp'),
    path('detailsp/<int:pk>/', detail_scholarship_for_sponsors, name='detailsp'),
    path('detail/<int:pk>/', detail_scholarship, name='detail'),
    url(r'^accounts/login/$', views.LoginView.as_view(), name='login'),
    url(r'^accounts/logout/$', views.LogoutView.as_view(), name='logout', kwargs={'next_page': '/'}),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
