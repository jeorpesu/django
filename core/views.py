from django.views.generic import View
# En Django, django.views.generic.View es una clase base que puedes utilizar 
# para crear tus propias vistas basadas en clases. Las vistas basadas en clases 
# son una forma alternativa de definir vistas en Django en comparación con 
# las vistas basadas en funciones.
# Al heredar de django.views.generic.View, puedes definir tus 
# propias vistas basadas en clases y aprovechar la funcionalidad 
# proporcionada por Django, como la capacidad de definir métodos 
# como get() y post() para manejar las solicitudes HTTP GET y POST, respectivamente.
from django.shortcuts import render
# En Django, django.shortcuts.render es una función que se utiliza 
# comúnmente para renderizar plantillas HTML y devolver una respuesta HTTP. 
# Esta función simplifica el proceso de renderización de plantillas al 
# proporcionar una forma rápida y conveniente de hacerlo.

class Homeview(View):
    def get(self,request,*args, **kwargs):
        context={
            
        }
        return render(request,'index.html',context)#aqui le estamos pasando lo que se va a ver por pantalla 
        #gracias a la configuracion previamente hecha se redirecciona a la carpeta templates
    
    
    
    
    
    
    
    
#     La función render toma tres argumentos:
# request: El objeto de solicitud HTTP que se pasa a la vista.
# 'mi_app/plantilla.html': La ruta a la plantilla HTML que se 
# utilizará para renderizar la respuesta. Django buscará esta plantilla 
# en los directorios especificados en la configuración de la aplicación.
# contexto: Un diccionario que contiene los datos que se pasan a
# la plantilla para ser renderizados dinámicamente.
# render carga la plantilla especificada, la rellena con los datos 
# del contexto y devuelve una respuesta HTTP con el contenido de la plantilla 
# renderizada. Esta respuesta se envía al navegador del cliente que realizó la solicitud.

# En resumen, render es una función útil en Django para renderizar plantillas HTML
# y generar respuestas HTTP dinámicas basadas en la lógica de la aplicación y los datos proporcionados.