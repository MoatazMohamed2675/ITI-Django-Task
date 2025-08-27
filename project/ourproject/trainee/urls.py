from django.urls import path
from .views import *

urlpatterns = [ 
    path('', allTrainee,name='alltrainee'),
    path('Update/<int:id>/', updateTrainee,name='updatetrainee'),
    path('Insert/', insertTrainee, name='inserttrainee'),
    path('Delete/<int:id>/', deleteTrainee,name='deletetrainee'),
]