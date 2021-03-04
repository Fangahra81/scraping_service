from django.db import models

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=25,
    verbose_name='Название населенного пункта')
    slug = models.CharField(max_length=25, blank=True)
    
    class Meta():
    
        verbose_name= 'Название населенного пункта'
        verbose_name_plural='Названия населенных пунктов'
    def __str__(self):
        return self.name
    