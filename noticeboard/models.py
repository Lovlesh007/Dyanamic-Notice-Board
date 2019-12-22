from django.db import models

# Create your models here.
class Update(models.Model):
	updation_regarding=models.CharField(max_length=100)
	any_important_message=models.CharField(max_length=500)
	deadline=models.CharField(max_length=100)
	noticeadddate =models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return str((self.updation_regarding,self.any_important_message,self.deadline,self.noticeadddate))
		