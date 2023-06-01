from django.urls import path
from sai.views import *

app_name='sai'

urlpatterns=[
    path('spec1/',spec1,name='spec1'),
]