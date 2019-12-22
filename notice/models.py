from django.db import models

# Create your models here.
class Mynotice(models.Model):
	information = models.CharField(max_length=35)
	def __str__(self):
	  return (self.information)