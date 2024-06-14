from django import forms
from models import Usuario, Publicacion, Comentario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [ 'nombre' , 'correo']

class PublicacionForm(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = [ 'titulo' , 'contenido' , 'autor']

class ComentarioForm(forms.Modelsform):
    class Meta:
        model = Comentario
        fields = ['contenido', 'autor' , 'publicacion' ]

from django.shortcuts import render, redirect
from .forms import UsuarioForm, PublicacionForm, ComentarioForm
from .models import Usuario, Publicacion, Comentario

def agregar_usuario(request):
    if request.method == 'POST' :
        form = UsuarioForm(request.POST)
        if form.is.valid():
            form.save()
            return redirect('index')
    else:
        form = PublicacionForm
    return render(request, 'agregar_publicacion.html', {'form': form})
