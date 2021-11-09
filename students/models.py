from django.db import models
from classes.models import BaseModel

# Create your models here.
class Student (BaseModel):
    nombre = models.CharField(max_length=100)
    correo = models.CharField(max_length=100, null=True)
    edad = models.IntegerField(null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True)

