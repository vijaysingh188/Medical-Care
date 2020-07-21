from django import forms
from django.forms import ModelForm
from accounts.models import CustomUser
from django.forms import inlineformset_factory

class UserForm(forms.ModelForm):
	doctor_options = (
		('Select Type','Select Type'),
		('DA','Allopathy'),
		('DB','Ayurveda'),
		('DC','Homoeopathy'),
		('DD','Unani'),
		('DE','Siddha'),
		('DF','Junior Doctor'),
		('DG','Front Desk'),
		)
	title = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder':'Title'}))
	first_name = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder':'First Name'}))
	middle_name = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder':'Middle Name'}))
	last_name = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder':'Last Name'}))
	type_of_doctor = forms.ChoiceField(required=False, choices=doctor_options)
	payment = forms.CharField(required=False)
	usecode = forms.CharField(required=False)
	house_no = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder':'House No'}))
	street = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder':'Street'}))
	area = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder':'Locality / Area / Pada'}))
	city = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder':'City / Town / Village'}))
	taluka = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder':'Taluka'}))
	district = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder':'District'}))
	state = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder':'State'}))
	pincode = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder':'Pin Code'}))
	country = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder':'Country'}))
	name_of_hospital = forms.CharField(required=False)
	owner_name = forms.CharField(required=False)
	no_of_doctor_accounts = forms.CharField(required=False)
	name_of_nursing_home = forms.CharField(required=False)

	class Meta:
		model = CustomUser
		fields = ['title','first_name','middle_name','last_name','type_of_doctor','payment','usecode','phone_no','email','house_no','street','area','city','taluka','district','state','pincode','country','name_of_hospital','no_of_doctor_accounts','owner_name','name_of_nursing_home']

class IndivdualDoctorProfileForm(forms.ModelForm):
	gender_options = (
		('Select Gender', 'Select Gender'),
		('M', 'Male'),
		('F', 'Female'),
		)

	gender = forms.ChoiceField(choices=gender_options)
	dob = forms.IntegerField()
	qualification = forms.CharField()
	speciality1 = forms.CharField()
	speciality2 = forms.CharField(required=False)
	speciality3 = forms.CharField(required=False)
	practicing_since = forms.CharField()
	reg_no_state = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'State'}))
	reg_no_number = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Number'}))
	reg_no_year = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Year'}))
	picture = forms.ImageField(widget=forms.FileInput)
	phone_no1 = forms.CharField()
	email1 = forms.CharField()
	landline_no = forms.CharField()
	landline_no1 = forms.CharField()
	res_house_no = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'House No'}))
	res_street = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Street'}))
	res_area = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Locality / Area / Pada'}))
	res_city = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'City / Town / Village'}))
	res_taluka = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Taluka'}))
	res_district = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'District'}))
	res_state = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'State'}))
	res_pincode = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Pin Code'}))
	res_country = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Country'}))


	class Meta:
		model = CustomUser
		fields = ['gender','dob','qualification','speciality1','speciality2','speciality3','practicing_since','reg_no_state','reg_no_number','reg_no_year','email1','picture','phone_no1','landline_no','landline_no1','res_state','res_country','res_pincode','res_district','res_street','res_area','res_taluka','res_house_no','res_city']

class NursingHomeProfileForm(forms.ModelForm):
	speciality1 = forms.CharField()
	speciality2 = forms.CharField(required=False)
	speciality3 = forms.CharField(required=False)
	reg_no_state = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'State'}))
	reg_no_number = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Number'}))
	reg_no_year = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Year'}))
	picture = forms.ImageField(widget=forms.FileInput)
	phone_no1 = forms.CharField()
	email1 = forms.CharField()
	landline_no = forms.CharField()

	class Meta:
		model = CustomUser
		fields = ['speciality1','speciality2','speciality3','reg_no_state','reg_no_number','reg_no_year','email1','picture','phone_no1','landline_no']

class HospitalProfileForm(forms.ModelForm):
	speciality1 = forms.CharField()
	speciality2 = forms.CharField(required=False)
	speciality3 = forms.CharField(required=False)
	reg_no_state = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'State'}))
	reg_no_number = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Number'}))
	reg_no_year = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Year'}))
	picture = forms.ImageField(widget=forms.FileInput)
	phone_no1 = forms.CharField()
	email1 = forms.CharField()
	landline_no = forms.CharField()

	class Meta:
		model = CustomUser
		fields = ['speciality1','speciality2','speciality3','reg_no_state','reg_no_number','reg_no_year','email1','picture','phone_no1','landline_no']

class IndivdualUserProfileForm(forms.ModelForm):
	gender_options = (
		('Select Gender', 'Select Gender'),
		('Male', 'Male'),
		('Female', 'Female'),
		)
	relationship_options = (
		('Select Relationship', 'Select Relationship'),
		('Mother', 'Mother'),
		('Father', 'Father'),
		('Daughter', 'Daughter'),
		('Son', 'Son'),
		('Wife', 'Wife'),
		('Husband', 'Husband'),
		('Brother', 'Brother'),
		('Sister', 'Sister'),
		)

	gender = forms.ChoiceField(choices=gender_options)
	dob = forms.DateField(widget=forms.DateInput(attrs={'id':'datepicker'}),required=False)
	phone_no1 = forms.CharField()
	email1 = forms.CharField()
	landline_no = forms.CharField()
	relationship = forms.ChoiceField(choices=relationship_options)
	relation_name = forms.CharField()
	relation_phone_no = forms.CharField()
	relation_email = forms.CharField()

	class Meta:
		model = CustomUser
		fields = ['gender','dob','phone_no1','email1','landline_no','relationship','relation_name','relation_phone_no','relation_email']

