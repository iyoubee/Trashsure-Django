"""project_django URL Configuration

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
from django.urls import path, include

urlpatterns = [
    path('secret/', admin.site.urls),
    path('', include('landing_page.urls')),
    path('dashboard/', include('user_dashboard.urls')),
    path('dashboard/prize', include('prize.urls')),
    path('dashboard/withdraw', include('withdraw.urls')),
    path('dashboard/deposit', include('deposit.urls')),
    path('admin/', include('admin_page.urls')),
    path("__reload__/", include("django_browser_reload.urls")),
]