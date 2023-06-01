from django.urls import path
from ssv.views import *

app_name='ssv'

urlpatterns=[
    path('spec3/',spec3,name='spec3'),
]