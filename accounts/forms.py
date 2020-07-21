from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.forms import ModelForm
from .models import SecurityQuestions, ModuleMaster, Contact, CustomUser, AddOnServices, pharamcytab, Emptytext, Labour, Empty
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
	class Meta(UserCreationForm):
		model = CustomUser
		fields = ('email',)


class CustomUserChangeForm(UserChangeForm):
	class Meta:
		model = CustomUser
		fields = ('email',)


class IndivdualUserForm(ModelForm):
	title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Title'}))
	first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'First Name'}))
	middle_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Middle Name'}))
	last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Last Name'}))
	phone_no = forms.CharField()
	email = forms.EmailField()
	password = forms.CharField(widget=forms.PasswordInput(attrs={'id':'pass_log_id'}),required=False)
	usecode = forms.CharField(required=False)
	class Meta:
		model = CustomUser
		fields = ['title','first_name','middle_name','last_name','phone_no','email','password','usecode']
	#def clean(self, *args,**kwargs):
	#	email = self.cleaned_data['email']
	#	if CustomUser.objects.filter(email=email).exists():
	#		raise ValidationError("Email already exists")
	#	return super(IndivdualUserForm, self).clean(*args, **kwargs)


class IndivdualDoctorForm(ModelForm):
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
	type_of_doctor = forms.ChoiceField(choices=doctor_options)
	title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Title'}))
	first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'First Name'}))
	middle_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Middle Name'}))
	last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Last Name'}))
	phone_no = forms.CharField()
	payment = forms.CharField(required=False)
	usecode = forms.CharField(required=False)
	email = forms.EmailField()
	password = forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model = CustomUser
		fields = ['type_of_doctor','title','first_name','middle_name','last_name','phone_no','payment','usecode','email','password']


class HospitalForm(ModelForm):
	name_of_hospital = forms.CharField()
	street = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Street'}))
	area = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Locality / Area / Pada'}))
	city = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'City / Town / Village'}))
	taluka = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Taluka'}))
	district = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'District'}))
	state = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'State'}))
	pincode = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Pin Code'}))
	country = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Country'}))
	owner_name = forms.CharField()
	phone_no = forms.CharField()
	email = forms.EmailField()
	no_of_doctor_accounts = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput())
	payment = forms.CharField(required=False)
	usecode = forms.CharField(required=False)
	class Meta:
		model = CustomUser
		fields = ['payment','usecode','name_of_hospital','street','area','city','taluka','district','state','pincode','country','owner_name','phone_no','email','no_of_doctor_accounts','password']

class NursingHomeForm(ModelForm):
	name_of_nursing_home = forms.CharField()
	street = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Street'}))
	area = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Locality / Area / Pada'}))
	city = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'City / Town / Village'}))
	taluka = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Taluka'}))
	district = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'District'}))
	state = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'State'}))
	pincode = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Pin Code'}))
	country = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Country'}))
	owner_name = forms.CharField()
	phone_no = forms.CharField()
	email = forms.EmailField()
	payment = forms.CharField(required=False)
	usecode = forms.CharField(required=False)
	no_of_doctor_accounts = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model = CustomUser
		fields = ['payment','usecode','name_of_nursing_home','street','area','city','taluka','district','state','pincode','country','owner_name','phone_no','email','no_of_doctor_accounts','password']


class UserLoginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Email'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}))


class SecurityQuestionsForm(ModelForm):
	question = forms.CharField(label='question', widget=forms.TextInput(attrs={'placeholder':'Security Question'}))
	answer = forms.CharField(label='answer', widget=forms.TextInput(attrs={'placeholder':'Answer'}))
	class Meta:
		model = SecurityQuestions
		fields = ['question','answer']

class PasswordForm(forms.Form):
	password = forms.CharField(disabled=True, widget=forms.PasswordInput(attrs={'placeholder':'New Password'}))
	password_confirm = forms.CharField(disabled=True, widget=forms.PasswordInput(attrs={'placeholder':'Re-enter Password'}))



class PasswordVerificationForm(forms.Form):
	question = forms.ModelChoiceField(disabled=True, queryset=SecurityQuestions.objects.all(), empty_label=None, widget=forms.Select(attrs={'class':'form-control','id': 'sectxt'}))
	answer = forms.CharField(disabled=True, label='answer', widget=forms.TextInput(attrs={'placeholder':'Answer','id': 'anstxt'}))
	phone_no = forms.CharField(disabled=True,label='phone_no', widget=forms.TextInput(attrs={'placeholder':'Enter OTP','id': 'otptxt'}))

class ModuleMasterForm(ModelForm):
	module_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Module Name'}))
	module_code = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Module Code'}))
	no_of_patients = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Number of Patients'}))
	web_space = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Mb'}))
	amount = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'in Rupees'}))
	cgst = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'%'}))
	sgst = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'%'}))
	gst = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'%'}))
	total_amount = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'in Rupees'}))

	class Meta:
		model = ModuleMaster
		fields = ['module_name','module_code','no_of_patients','web_space','amount','cgst','sgst','gst','total_amount']


class ContactForm(ModelForm):
	name = forms.CharField()
	phone_no = forms.CharField()
	email = forms.CharField()
	message = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'cols': 5}))

	class Meta:
		model = Contact
		fields = ['name','phone_no','email','message']

class AddServices(ModelForm):
	add_onservices = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Add_on service'}),required=False)
	add_on_servicescode = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Add-on Services Code'}),required=False)
	amount = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'amount'}),required=False)
	cgst = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'%'}),required=False)
	sgst = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'%'}),required=False)
	gst = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'%'}),required=False)
	total_amount = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'in Rupees'}),required=False)

	class Meta:
		model = AddOnServices
		fields = ['add_onservices','add_on_servicescode','amount','cgst','sgst','gst','total_amount']




class pharamcy(ModelForm):
   companyname=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'name'}))
   addresslineone=forms.CharField(required=False)
   addresslinetwo = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'address'}),required=False)
   streetname = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'streetname'}),required=False)
   city = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'city'}),required=False)
   country = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'country'}),required=False)
   state = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'state'}),required=False)
   pincode = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':'pincode'}),required=False)
   nationalhead = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'nationalhead'}),required=False)
   contactnumber = forms.CharField(required=False)
   emailaddress = forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'email'}),required=False)
   phonenumber = forms.CharField(required=False)
   regionalhead =forms.CharField(widget=forms.TextInput(attrs= {'placeholder':'head'}),required=False)
   regionalcontactnumber = forms.CharField(required=False)
   regionalemailaddress = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'email'}),required=False)
   regionalphonenumber = forms.CharField(required=False)
   scientifichead = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'head'}),required=False)
   scientificcontactnumber = forms.CharField()
   scientificemailaddress = forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'email'}),required=False)
   scientificphonenumber = forms.CharField(required=False)

   class Meta:
       model = pharamcytab
       fields = ['companyname','addresslineone','addresslinetwo','streetname','city','country','state','pincode','nationalhead','contactnumber','emailaddress','phonenumber','regionalhead','regionalcontactnumber','regionalemailaddress','regionalphonenumber','scientifichead','scientificcontactnumber','scientificemailaddress','scientificphonenumber']


class laboratorylab(ModelForm):

   investigationname=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'name'}))
   synonyms=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Synonyms'}),required=False)
   importantnotes=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'importantnotes'}),required=False)
   GENDER_CHOICES=(
    	('Yes-No','Yes-No'),
	    ('Present-Absent','Present-Absent'),
	    ('Seen-Not','Seen-Not Seen'),
	    ('Positive-Negative','Positive-Negative'),
	    ('Customize-Value','Customize-Value'),
   )
   selectdropdownlist=forms.ChoiceField(choices=GENDER_CHOICES,widget=forms.RadioSelect(),required=False)
   select=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'select'}),required=False)
   froms=forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':'date in days'}),required=False)
   to = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':'end date'}),required=False)
   gender= forms.CharField(widget=forms.TextInput(attrs={'placeholder':'gender'}),required=False)
   umo1= forms.CharField(widget=forms.TextInput(attrs={'placeholder':'umo1'}),required=False)
   umo2 = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'umo2'}),required=False)
   conversationfactor= forms.CharField(widget=forms.TextInput(attrs={'placeholder':'factor'}),required=False)
   GEEKS_CHOICES=(
      ('high','True'),
      ('low','False'),
   )

   refrencerange = forms.ChoiceField(choices=GEEKS_CHOICES,widget=forms.RadioSelect(),required=False)
   GENDER_CHOICES=(
      ('high','True'),
      ('low','False'),
   )
   high = forms.ChoiceField(choices=GENDER_CHOICES,widget=forms.RadioSelect(),required=False)
   class Meta:
      model=Labour
      fields=['id','investigationname','synonyms','importantnotes','selectdropdownlist','select','froms','to','gender','umo1','umo2','conversationfactor','refrencerange','high']
class labo(ModelForm):
   Labour=forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':'date in days'}),required=False)
   froms=forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':'date in days'}),required=False)
   to = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':'end date'}),required=False)
   gender= forms.CharField(widget=forms.TextInput(attrs={'placeholder':'gender'}),required=False)
   umo1= forms.CharField(widget=forms.TextInput(attrs={'placeholder':'umo1'}),required=False)
   umo2 = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'umo2'}),required=False)
   conversationfactor= forms.CharField(widget=forms.TextInput(attrs={'placeholder':'factor'}),required=False)
   GEEKS_CHOICES=(
      ('high','True'),
      ('low','False'),
   )

   refrencerange = forms.ChoiceField(choices=GEEKS_CHOICES,widget=forms.RadioSelect(),required=False)
   GENDER_CHOICES=(
      ('high','True'),
      ('low','False'),
   )
   high = forms.ChoiceField(choices=GENDER_CHOICES,widget=forms.RadioSelect(),required=False)


   class Meta:
      model=Emptytext
      fields=['id','Labour','froms','to','gender','umo1','umo2','conversationfactor','refrencerange','high']


class labo1(ModelForm):
   Labour=forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':'date in days'}),required=False)
   froms=forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':'date in days'}),required=False)
   to = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':'end date'}),required=False)
   gender= forms.CharField(widget=forms.TextInput(attrs={'placeholder':'gender'}),required=False)
   umo1= forms.CharField(widget=forms.TextInput(attrs={'placeholder':'umo1'}),required=False)
   umo2 = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'umo2'}),required=False)
   conversationfactor= forms.CharField(widget=forms.TextInput(attrs={'placeholder':'factor'}),required=False)
   GEEKS_CHOICES=(
      ('high','True'),
      ('low','False'),
   )

   refrencerange = forms.ChoiceField(choices=GEEKS_CHOICES,widget=forms.RadioSelect(),required=False)
   GENDER_CHOICES=(
      ('high','True'),
      ('low','False'),
   )
   high = forms.ChoiceField(choices=GENDER_CHOICES,widget=forms.RadioSelect(),required=False)


   class Meta:
      model=Empty
      fields=['id','Labour','froms','to','gender','umo1','umo2','conversationfactor','refrencerange','high']


