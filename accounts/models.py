from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from .managers import CustomUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
import requests

class CustomUser(AbstractUser):
	username = None
	email = models.EmailField(_('email address'), unique=True)
	title = models.CharField(max_length=10, blank=True, null=True)
	middle_name = models.CharField(max_length=255, blank=True, null=True)
	phone_no = models.CharField(max_length=255)
	payment = models.CharField(max_length=255, blank=True, null=True)
	usecode = models.CharField(max_length=255, blank=True, null=True)
	type_of_doctor = models.CharField(max_length=255, blank=True, null=True)
	name_of_hospital = models.CharField(max_length=255, blank=True, null=True)
	street = models.CharField(max_length=255, blank=True, null=True)
	area = models.CharField(max_length=255, blank=True, null=True)
	city = models.CharField(max_length=255, blank=True, null=True)
	taluka = models.CharField(max_length=255, blank=True, null=True)
	district = models.CharField(max_length=255, blank=True, null=True)
	state = models.CharField(max_length=255, blank=True, null=True)
	pincode = models.CharField(max_length=255, blank=True, null=True)
	country = models.CharField(max_length=255, blank=True, null=True)
	owner_name = models.CharField(max_length=255, blank=True, null=True)
	no_of_doctor_accounts = models.CharField(max_length=255, blank=True, null=True)
	name_of_nursing_home = models.CharField(max_length=255, blank=True, null=True)
	is_individual = models.BooleanField(default=False)
	is_hdc_individual = models.BooleanField(default=False)
	is_hdc_hospital = models.BooleanField(default=False)
	is_hdc_nursing_home = models.BooleanField(default=False)
	special_id = models.CharField(max_length=255, null=True, default=None)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []

	objects = CustomUserManager()

	def save(self,*args, **kwargs):
		if not self.special_id:
			if self.type_of_doctor == "DA":
				prefix = 'DA{}'.format(timezone.now().strftime('%y%m%d'))
			elif self.type_of_doctor == "DB":
				prefix = 'DB{}'.format(timezone.now().strftime('%y%m%d'))
			elif self.type_of_doctor == "DC":
				prefix = 'DC{}'.format(timezone.now().strftime('%y%m%d'))
			elif self.type_of_doctor == "DD":
				prefix = 'DD{}'.format(timezone.now().strftime('%y%m%d'))
			elif self.type_of_doctor == "DE":
				prefix = 'DE{}'.format(timezone.now().strftime('%y%m%d'))
			elif self.type_of_doctor == "DF":
				prefix = 'DF{}'.format(timezone.now().strftime('%y%m%d'))
			elif self.type_of_doctor == "DG":
				prefix = 'DG{}'.format(timezone.now().strftime('%y%m%d'))
			else:
				prefix = 'AA{}'.format(timezone.now().strftime('%y%m%d'))
			prev_instances = self.__class__.objects.filter(special_id__contains=prefix)
			if prev_instances.exists():
				last_instance_id = prev_instances.last().special_id[-4:]
				self.special_id = prefix+'{0:04d}'.format(int(last_instance_id)+1)
			else:
				self.special_id = prefix+'{0:04d}'.format(1)
		super(CustomUser, self).save(*args, **kwargs)

	def __str__(self):
		return self.email


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

class AddOnServices(models.Model):
	add_onservices = models.CharField(max_length=255)
	add_on_servicescode = models.CharField(max_length=255)
	amount = models.FloatField(default = 0)
	cgst = models.FloatField(default = 0)
	sgst = models.FloatField(default = 0)
	gst = models.FloatField(default = 0)
	total_amount = models.FloatField(default = 0)

	def __str__(self):
		return self.add_onservices

class pharamcytab(models.Model):
	companyname = models.CharField(max_length=255)
	addresslineone=models.CharField(max_length=255)
	addresslinetwo = models.CharField(max_length=255)
	streetname = models.CharField(max_length=255)
	city= models.CharField(max_length=255)
	country= models.CharField(max_length=266)
	state= models.CharField(max_length=255)
	pincode= models.IntegerField(default = 0)
	nationalhead= models.CharField(max_length=266)
	contactnumber= models.CharField(max_length=255, blank=True)
	emailaddress= models.EmailField()
	phonenumber= models.CharField(max_length=255, blank=True)
	regionalhead= models.CharField(max_length=255)
	regionalcontactnumber= models.CharField(max_length=255, blank=True)
	regionalemailaddress= models.CharField(max_length=255)
	regionalphonenumber= models.CharField(max_length=255, blank=True)
	scientifichead=models.CharField(max_length=266)
	scientificcontactnumber= models.CharField(max_length=255, blank=True)
	scientificemailaddress= models.EmailField()
	scientificphonenumber=models.CharField(max_length=255, blank=True)
	def __str__(self):
		return self.city

class Emptytext(models.Model):
	GENDER_CHOICES=(
		('high','high'),
		('low','low'),
		)
	GENDER_CHOICES=(
		('high','high'),
		('low','low'),
		)
	Labour=models.ForeignKey('Labour',on_delete=models.CASCADE,related_name='Emptytext')
	froms= models.IntegerField()
	to = models.IntegerField()
	gender= models.CharField(max_length=255,blank=True)
	umo1= models.CharField(max_length=255,blank=True)
	umo2 = models.CharField(max_length=255,blank=True)
	conversationfactor= models.CharField(max_length=255)
	refrencerange = models.CharField(choices=GENDER_CHOICES,max_length=10,verbose_name=umo1)
	high=models.CharField(choices=GENDER_CHOICES,max_length=10)


	def __unicode__(self):
		return u'%s' % (self.gender)
	class Meta:
		verbose_name=('gender')
		verbose_name_plural=("gender")

class Labour(models.Model):
	GENDER_CHOICES=(
		('Yes-No','Yes-No'),
		('Present-Absent','Present-Absent'),
		('Seen-Not','Seen-Not Seen'),
		('Positive-Negative','Positive-Negative'),
		('Customize-Value','Customize-Value'),
		)
	investigationname=models.CharField(max_length=255)
	synonyms = models.CharField(max_length=255)
	importantnotes = models.CharField(max_length=255)
	selectdropdownlist=models.CharField(choices=GENDER_CHOICES,max_length=20)
	select=models.CharField(max_length=255)

	def __str__(self):
		return self.investigationname

	def __unicode__(self):
		return self.investigationname

class Empty(models.Model):
	laboratory_id=models.ForeignKey('Labour',on_delete=models.CASCADE)
	froms= models.IntegerField()
	to = models.IntegerField()
	gender= models.CharField(max_length=255)
	umo1= models.CharField(max_length=255)
	umo2 = models.CharField(max_length=255)
	conversationfactor= models.CharField(max_length=255)
	refrencerange=models.CharField(max_length=255)
	high=models.CharField(max_length=244)

	def __str__(self):
		return self.gender

class Coupon(models.Model):
	PROFILE_CHOICES = (
		('is_individual', 'is_individual'),
		('is_hdc_individual', 'is_hdc_individual'),
		('is_hdc_hospital', 'is_hdc_hospital'),
		('is_hdc_nursing_home', 'is_hdc_nursing_home')

	)
	code = models.CharField(max_length=6)
	startDate = models.DateField()
	endDate = models.DateField()
	count_value = models.IntegerField(default=100)
	profileChoices = models.CharField(choices=PROFILE_CHOICES, max_length=20)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	active = models.BooleanField(default=True)

	def __str__(self):
		return self.code
