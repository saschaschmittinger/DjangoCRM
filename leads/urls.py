from django.urls import path
from .views import *

app_name = 'leads'

urlpatterns =[
    path('',home_view, name='home_view')
]