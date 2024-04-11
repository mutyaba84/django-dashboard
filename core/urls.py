"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import include, path


from users import views as user_views
from recipients import views
from django.urls import path
from currency_converter import views


urlpatterns = [
    path('', include('home.urls')),
    path("admin/", admin.site.urls),
    path("", include('admin_soft.urls')),
   # path('register/', user_views.register, name='register'),
    #path('', include('users.urls')),
    path('transfers/', include('transfers.urls')),
    path('currency/', include('currency_converter.urls')),
    path('payments/', include('payments.urls')),
    path('recipients/', include('recipients.urls')),
    path('service-providers/', include('service_providers.urls')),# Include app URLs here
    path('', include('email_notifications.urls')),
    path('currency-converter/', include('currency_converter.urls')),
    
    # urls.py


    path('exchange-rate/', views.exchange_rate_form, name='exchange_rate_form'),
    # Other URL patterns for your application

]


