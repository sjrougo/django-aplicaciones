from django.urls import path
from applications.users.views import *

urlpatterns = [
    path('endpoint1/', endpoint1_users)
]