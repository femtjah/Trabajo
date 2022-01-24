from django.db import models

# Create your models here.

class Movie(models.Model):
    id = models.AutoField(primary_key= True)
    name = models.CharField('Nombre Pelicula', max_length=150,unique=True,blank=False, null=False)
    description=models.CharField('Descripción',null=False, blank=False)
    image = models.ImageField('Imagen pelicula', upload_to='media/movie/', blank=True, null=True)
    created_date=models.DateField('Fecha de creación', auto_now=False, auto_now_add=True)
    modified_date = models.DateField('Fecha de modificación', auto_now=True, auto_now_add=False)
    deleted_date = models.DateField('Fecha de elimicación', auto_now=True, auto_now_add=False)

    class Meta:

        verbose_name = 'Pelicula'
        verbose_name_plural = 'Peliculas'

    def __str__(self):
        return self.name
