from django.urls import path
from applications.foro.views import *

urlpatterns = [
    path('endpoint1/', endpoint1_foro)
]