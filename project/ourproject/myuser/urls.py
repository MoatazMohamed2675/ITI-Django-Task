from django.urls import path 
from .views import *
urlpatterns = [
    path('Login/', Login),
    path('logout/', logout),
    path('register/', register),
]