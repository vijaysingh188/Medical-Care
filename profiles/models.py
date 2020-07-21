from django.db import models
from accounts.models import CustomUser

class IndivdualDoctorProfile(models.Model):
	user = models.OneToOneField('accounts.CustomUser', on_delete= models.CASCADE)
	gender = models.CharField(max_length=50)
	dob = models.CharField(max_length=150)
	qualification = models.CharField(max_length=150)
	speciality1 = models.CharField(max_length=150)
	speciality2 = models.CharField(max_length=150)
	speciality3 = models.CharField(max_length=150)
	practicing_since = models.CharField(max_length=150)
	reg_no_state = models.CharField(max_length=150)
	reg_no_number = models.CharField(max_length=150)
	reg_no_year = models.CharField(max_length=150)
	picture = models.ImageField(upload_to='doctor_document', blank=True)
	phone_no1 = models.CharField(max_length=150)
	email1 = models.CharField(max_length=150)
	landline_no = models.CharField(max_length=150)
	landline_no1 = models.CharField(max_length=150)
	res_house_no = models.CharField(max_length=150)
	res_street = models.CharField(max_length=150)
	res_area = models.CharField(max_length=150)
	res_city = models.CharField(max_length=150)
	res_taluka = models.CharField(max_length=150)
	res_district = models.CharField(max_length=150)
	res_state = models.CharField(max_length=150)
	res_pincode = models.CharField(max_length=150)
	res_country = models.CharField(max_length=150)

	def __str__(self):
		return self.user.username

class NursingHomeProfile(models.Model):
	user =models.OneToOneField('accounts.CustomUser', on_delete= models.CASCADE)
	speciality1 = models.CharField(max_length=150)
	speciality2 = models.CharField(max_length=150)
	speciality3 = models.CharField(max_length=150)
	reg_no_state = models.CharField(max_length=150)
	reg_no_number = models.CharField(max_length=150)
	reg_no_year = models.CharField(max_length=150)
	picture = models.ImageField(upload_to='doctor_document', blank=True)
	phone_no1 = models.CharField(max_length=150)
	email1 = models.CharField(max_length=150)
	landline_no = models.CharField(max_length=150)

	def __str__(self):
		return self.user.username

class HospitalProfile(models.Model):
	user =models.OneToOneField('accounts.CustomUser', on_delete= models.CASCADE)
	speciality1 = models.CharField(max_length=150)
	speciality2 = models.CharField(max_length=150)
	speciality3 = models.CharField(max_length=150)
	reg_no_state = models.CharField(max_length=150)
	reg_no_number = models.CharField(max_length=150)
	reg_no_year = models.CharField(max_length=150)
	picture = models.ImageField(upload_to='doctor_document', blank=True)
	phone_no1 = models.CharField(max_length=150)
	email1 = models.CharField(max_length=150)
	landline_no = models.CharField(max_length=150)

	def __str__(self):
		return self.user.username

class IndivdualUserProfile(models.Model):
	user =models.OneToOneField('accounts.CustomUser', on_delete= models.CASCADE)
	first_name = models.CharField(max_length=150)
	last_name = models.CharField(max_length=150)
	middle_name = models.CharField(max_length=150)
	gender = models.CharField(max_length=50)
	dob = models.CharField(max_length=150)
	phone_no1 = models.CharField(max_length=150)
	email1 = models.CharField(max_length=150)
	landline_no = models.CharField(max_length=150)
	relationship = models.CharField(max_length=150)
	relation_name = models.CharField(max_length=150)
	relation_phone_no = models.CharField(max_length=150)
	relation_email = models.CharField(max_length=150)

	def __str__(self):
		return self.email1
