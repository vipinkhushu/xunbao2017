from django.db import models
from datetime import datetime

class question ( models.Model):
	description =models.CharField(max_length=500)
	answer = models.CharField(max_length=50)
	level = models.IntegerField(default=1)

	def __str__(self):
		return str(self.level) +" "+self.description

class player(models.Model):
	fb_id = models.CharField(max_length=50)
	name = models.CharField(max_length=250)
	level = models.IntegerField(default=1)
	created_on = models.DateTimeField(default=datetime.now(),blank=True)
	email_id = models.EmailField(max_length=250,default="abc@gmail.com" ,blank=True,null=True)

	def levelup(self):
		self.level+=1

	def __str__(self):
		return self.name +" - level "+str(self.level)

class message(models.Model):
	message=models.CharField(max_length=250)
	flag = models.IntegerField(default=0)

	def __str__(self):
		return self.message

class logs(models.Model):
	fb_id = models.CharField(max_length=50)
	name = models.CharField(max_length=250)
	level = models.BigIntegerField(default=1)
	answer = models.CharField(max_length=250)
	created_on = models.DateTimeField(default=datetime.now(),blank=True)

	def __str__(self):
		return self.name +" "+str(self.level) + " "+self.answer
