"""
URL configuration for assignment1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from sai.views import * 
from shankar.views import *
from vemula.views import *
from ssv.views import *
import sai,shankar,ssv,vemula

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gen1/',gen1,name='gen1'),
    path('gen2/',gen2,name='gen2'),
    path('gen3/',gen3,name='gen3'),
    path('gen4/',gen4,name='gen4'),
    path('sai/',include('sai.urls')),
    path('shankar/',include('shankar.urls')),
    path('ssv/',include('ssv.urls')),
    path('vemula/',include('vemula.urls')),

]
