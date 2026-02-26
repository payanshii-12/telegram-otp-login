"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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


# accounts/urls.py
from django.urls import path
from .views import ( send_otp_view ,verify_otp_view , login_page, login_history_view)

urlpatterns = [
    path('login/', login_page , name="login"),
    path('otp/send/', send_otp_view , name="send_otp"),
    path('otp/verify/', verify_otp_view, name="verify_otp"),
    path('login-history/<str:phone_number>/', login_history_view ),
]

