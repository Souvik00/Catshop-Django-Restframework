from django.db import models

# Create your models here.

class CatShop(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    breed = models.CharField(max_length=50)
    description = models.TextField(max_length=50)
    #attribute of the model cats

    def __str__(self):
        return self.name
    #return the name of the model