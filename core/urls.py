
from django.contrib import admin
from django.urls import path, include#Para incluir el nuevo proyecto de blog se le agrega include   

#urls de admin
#importando una subclase desde la carpeta settings.py
from .views import Homeview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Homeview.as_view(),name='home'),#sintaxis para mostrar lo que se hizo nuevo 
    path('blog/',include('blog.urls',namespace='blog'))
]
