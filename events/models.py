from django.db import models
# Create your models here.
class Mymodel(models.Model):
	myfield = models.CharField(max_length=35)
	#programadddate =models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return (self.myfield)

#must be inside the class and this is double underscore
#this is outside the function		        


  #variablename= models.IntegerField()
  #            = models.CharField(max_length=35)
  #            =models.FloatField()  

class Mymodel2(models.Model):
	myfield2 = models.CharField(max_length=35)
	def __str__(self):
		return (self.myfield2)

class Mymodel3(models.Model):
	myfield3 = models.IntegerField()
	def __str__(self):
		return (self.myfield3)

class Email(models.Model):
	my_email_from = models.CharField(max_length=35)
	#my_pass = models.CharField(max_length=35)
	my_email_to = models.CharField(max_length=35)
	my_email_cc = models.CharField(max_length=35)
	my_email_sub =models.CharField(max_length=35)
	my_email_compose =models.CharField(max_length=400)
	#my_pin = models.IntegerField()
	def __str__(self):
		return str((self.my_email_from,self.my_email_to,self.my_email_cc,self.my_email_sub,self.my_email_compose))


'''import datetime

from django.db import models
from django.utils import timezone

'''
'''class Question(models.Model):
    # ...
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)'''