from django.urls import path
from vemula.views import *

app_name='vemula'

urlpatterns=[
    path('spec4/',spec4,name='spec4'),
]