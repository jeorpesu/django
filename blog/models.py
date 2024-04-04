from django.db import models

# Create your models here.
class Post(models.Model):#esto se hace para crear un modelo
    
    title=models.CharField(max_length=250)#esto es un campo de caracteres 
    content=models.TextField()#campo de texto mas grande para excribir mas contenido
    
    def __str__(self):
        return self.title
    #MODELO CREADO