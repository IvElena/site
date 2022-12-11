from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', one_page),
    path('page/', page),
    path('', include('menu.urls'))

]
