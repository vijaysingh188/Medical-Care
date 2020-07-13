from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.forms import ModelForm
from .models import SecurityQuestions, ModuleMaster, Contact

User = get_user_model()

class UserLoginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'User Name'}))
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
