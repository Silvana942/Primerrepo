from django.db import models
from django.db.models.fields.related import ForeignKey, ManyToManyField
from django.db.models.deletion import SET_DEFAULT, SET_NULL
# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=200, null=False, blank=False, unique=True)
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

class Post(models.Model):
    titulo = models.CharField('Titulo', max_length=200, null=False, blank=False)
    descripcion = models.TextField('Descripcion' ,null=False, blank=False)
    fecha_creacion = models.DateTimeField('Fecha de creacion', auto_now_add = True)
    fecha_modificacion = models.DateTimeField('Fecha de modificacion', auto_now = True)
    categoria = ForeignKey(Categoria, on_delete=models.CASCADE, null=True, blank=False)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posteos'
        ordering = ['titulo']

    def __str__(self):
        return self.titulo


