"""
URL configuration for ServiceProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from serviceapp.views import index,user_signup,loginview,servicer_signup
from serviceapp import admin_urls, customer_urls, servicer_urls, worker_urls
from serviceapp import views

urlpatterns = [
    path('',index.as_view(),name='index'),
    path('admin/',admin_urls.urls()),
    path('user/',customer_urls.urls()),
    path('servicer/',servicer_urls.urls()),
    path('worker/',worker_urls.urls()),
    path('login/',loginview.as_view(),name='login'),
    path('usersignup',user_signup.as_view(),name='usersignup'),
    path('signup',servicer_signup.as_view(),name='signup'),
    path("logout_user", views.logout_user, name='logout_user'),
    path('Paymentcheckout/<int:id>',views.Paymentcheckout,name='Paymentcheckout'),
    path('Chpayments/<int:id>',views.Chpayments,name='Chpayments'),




   
]
if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
