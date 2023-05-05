from django.contrib import admin
from django.urls import path

from .views import index, feedback, saveComment, createpassword, sendemail

urlpatterns = [
    path('feedback/', feedback, name='feedback'),
    path('index/', index, name='index'),
    path('contacts/', saveComment, name='contacts'),
    path('createpassword/', createpassword, name='createpassword'),
    # path('send/', sendemail, name='send'),
]