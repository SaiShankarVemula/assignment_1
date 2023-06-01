from django.urls import path
from shankar.views import *

app_name='shankar'

urlpatterns=[
    path('spec2/',spec2,name='spec2'),
]