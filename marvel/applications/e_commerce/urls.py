from django.urls import path
from applications.e_commerce.views import *

urlpatterns = [
    path('endpoint1/', endpoint1_e_commerce),
    path('endpoint2/', endpoint2_e_commerce),
]