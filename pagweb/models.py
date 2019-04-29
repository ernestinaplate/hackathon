from django.db import models
from django.utils import timezone

'''
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
'''


# Create your models here.

class Freelancer(models.Model):
    PROFESIONES = (
        ('Fotografo', 'Fotografo'),
        ('Programador', 'Programador'),
        ('Profesor particular', 'Profesor particular'),
    )

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=50)
    foto_de_perfil = models.ImageField(upload_to='media/', null=True, blank=True)
    profesion = models.CharField(max_length=30, choices=Profesion.objects.all())
    email = models.EmailField()
    domicilio = models.TextField( null=True, blank=True)
    telefono = models.CharField(max_length=15, null=True, blank=True)
    exp_previa = models.TextField(null=True, blank=True)
    descripcion = models.TextField( null=True, blank=True)
    fotoportfolio = models.ImageField(upload_to='media/', null=True, blank=True)

    def __str__(self):
        return str(self.nombre) + ' ' + str(self.apellido) 
    
class Profesion(models.Model):
    nombre_profesion = models.CharField(max_lenght=30)

    def __str__(self):
        return str(self.nombre_profesion)




