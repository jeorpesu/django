from django.urls import path
from .views import BlogListView#aqui volvemos a importar la subclase pero esta vez de blog 
app_name='blog'

urlpatterns = [
    path('rama/',BlogListView.as_view(),name='url de blog')#aqui se le puede dar nombre a cada pagina de la aplicacion
]#recuerda colocar el .asview porque es una sub clase si no bota error 
