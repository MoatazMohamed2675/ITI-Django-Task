from django.urls import path
from .views import *
urlpatterns = [ 
    path('', allTracks,name='alltracks'),
    path('update/<int:id>/', updateTrack,name='updateTrack'),
    path('insert/', insertTrack, name='insertTrack'),
    path('delete/<int:id>/', deleteTrack,name='deleteTrack'),
]