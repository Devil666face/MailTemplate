
from .views import *
from django.urls import path

urlpatterns = [
    # path('', Home.as_view(), name='home'),
    path('template/<int:pk>', ViewTemplate.as_view(), name='template'),
    path('', HomeView.as_view(), name='home'),
]
