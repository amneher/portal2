from django.db import models


class main_site (models.Model):
   field_name = models.CharField(max_length=20, help_text='Enter field documentation')

 

   def __str__(self):
       return self.field