from django.db import models

# Create your models here.

class Brand(models.Model):
    brand_name = models.CharField(max_length=25)
    slug = models.SlugField(max_length=100,unique=True,null=True,blank=True)

    def __str__(self):
        return self.brand_name