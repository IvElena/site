from django.urls import path
from .views import *

urlpatterns = [
    path('menu/',menu),
    path('Vtorie_bluda/', Vtorie_bluda),
    path('Napitki/', Napitki),


]
