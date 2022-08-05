"""myprojects URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,include

urlpatterns = [

    path('', include('Teaflower.urls')),
    path('htp/', include('Http_add3.urls')),
    path('first', include('Firstapp_1.urls')),
    path('dtl1', include('DTL_2.urls')),
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
]
