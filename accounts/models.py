from django.db import models

class SecurityQuestions(models.Model):
	question = models.CharField(max_length=255, blank=True)
	answer = models.CharField(max_length=255, blank=True)

	def __str__(self):
	    return self.question

class ModuleMaster(models.Model):
	module_name = models.CharField(max_length=255, blank=True)
	module_code = models.CharField(max_length=255, blank=True)
	no_of_patients = models.IntegerField(default = 0)
	web_space = models.IntegerField(default = 0)
	amount = models.IntegerField(default = 0)
	cgst = models.IntegerField(default = 0)
	sgst = models.IntegerField(default = 0)
	gst = models.IntegerField(default = 0)
	total_amount = models.IntegerField(default = 0)
	updated_on = models.DateTimeField(auto_now=True)
	created_on = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.module_name

class Contact(models.Model):
	name = models.CharField(max_length=255, blank=True)
	phone_no = models.CharField(max_length=255, blank=True)
	email = models.EmailField(max_length=255, blank=True)
	message = models.CharField(max_length=255, blank=True)

	def __str__(self):
		return self.name