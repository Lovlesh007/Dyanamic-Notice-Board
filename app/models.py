from django.db import models
import datetime
from django.utils import timezone
# Create your models here.
class Question(models.Model):
	question_text = models.CharField(max_length=100)
	pub_date = models.DateTimeField('Date Published')	
	def __str__(self):
		return str((self.question_text,self.pub_date))


class Choice(models.Model):
 	question = models.ForeignKey(Question,on_delete=models.CASCADE)
 	choice_text = models.CharField(max_length=200)
 	votes = models.IntegerField(default=0)
 	def __str__(self):
 		return str((self.question,self.choice_text,self.votes))



