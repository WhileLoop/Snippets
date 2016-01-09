from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class SalesItem(models.Model):
   title = models.CharField(max_length=200)
   description = models.CharField(max_length=800)
   price = models.IntegerField()
   image = models.ImageField(upload_to = 'uploads/')

   def __str__(self):
       return self.title
