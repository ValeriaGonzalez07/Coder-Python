from django.http import HttpResponse
def saludo(request):
    return HttpResponse("Hola Django - Coder")
from django.db import models

class Usuario(models.Model):
    nombre = models.CharField
    correo = models.EmailField

    def __str__(self):
        return self.nombre
    
class Publicacion(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
    
class Comentario(models.Model):
    contenido = models.TextField()
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE)
    fecha_comentario = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comentario por {self.autor} en {self.publicacion}'