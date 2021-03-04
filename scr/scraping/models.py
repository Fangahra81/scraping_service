from django.db import models

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=25,
    verbose_name='Название населенного пункта', unique=True)
    slug = models.CharField(max_length=25, blank=True, unique=True)
    
    class Meta():
    
        verbose_name= 'Название населенного пункта'
        verbose_name_plural='Названия населенных пунктов'
    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=25,
                            verbose_name='Язык програмирования', unique=True)
    slug = models.CharField(max_length=25, blank=True)

    class Meta():
        verbose_name = 'Язык програмирования'
        verbose_name_plural = 'Языки програмирования'

    def __str__(self):
        return self.name
