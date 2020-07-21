from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, get_user_model, login, logout
from .forms import UserLoginForm, SecurityQuestionsForm, PasswordForm, IndivdualUserForm, IndivdualDoctorForm, HospitalForm, NursingHomeForm, ModuleMasterForm, ContactForm, PasswordVerificationForm, AddServices, pharamcy, laboratorylab, labo, labo1
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .models import SecurityQuestions, ModuleMaster, Contact, CustomUser, AddOnServices, pharamcytab, Labour, Emptytext, Empty
from django.http import Http404
from django.http import Http404
from django.contrib import messages
from django.http import JsonResponse
import requests
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.mail import EmailMessage
import datetime
import json
from .decorators import superadmin_required
from profiles.models import IndivdualDoctorProfile, NursingHomeProfile, HospitalProfile, IndivdualUserProfile
# from django.contrib.auth.forms import SetPasswordForm


@csrf_exempt
def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		name = request.POST.get('name')
		print(form.errors)
		if form.is_valid():
			if form.save():
				return redirect('/contact', messages.success(request, 'Thank you for contacting Us. Our team will contact you as soon as earliest.', 'alert-success'))
			else:
				return redirect('/contact', messages.error(request, 'Something went wrong!', 'alert-danger'))
		else:
			return redirect('/contact', messages.error(request, 'Form is not valid', 'alert-danger'))
	else:
		form = ContactForm()
		return render(request, "Contact_Us.html", {'form': form})


@login_required
@csrf_exempt
def contact_master(request):
	module = Contact.objects.all()
	return render(request, "Contact_Us_List.html", {'module': module})


@csrf_exempt
def home(request):
	return render(request, "index.html", {})


def activate_account(request, uidb64, token):
	try:
		uid = force_bytes(urlsafe_base64_decode(uidb64))
		user = CustomUser.objects.get(pk=uid)
	except(TypeError, ValueError, OverflowError, User.DoesNotExist):
		user = None
	if user is not None and account_activation_token.check_token(user, token):
		user.is_active = True
		user.save()
		login(request, user)
		return redirect('/existing_module_master', messages.success(request, 'Your account has been activated successfully!', 'alert-success'))
	else:
		return redirect('/register', messages.error(request, 'Activation link is invalid!', 'alert-danger'))

# https://www.google.com/settings/security/lesssecureapps


@csrf_exempt
def register(request):
	next = request.GET.get('next')

	if 'individualdoctor' in request.POST:
		form1 = IndivdualDoctorForm(request.POST)
		if form1.is_valid():
			user = form1.save(commit=False)
			password = form1.cleaned_data.get('password')
			type = form1.cleaned_data.get('type_of_doctor')
			user.type_of_doctor = type
			user.set_password(password)
			user.is_hdc_individual = True
			user.save()
			email_subject = 'Welcome To Health Perigon!'
			valid_till = (datetime.datetime.now() + datetime.timedelta(days=364)).date()
			date = json.dumps(valid_till, indent=4, sort_keys=True, default=str)
			type1 = "HDC - Individual Doctor"
			message = render_to_string('activate_account.html', {
				'user': user,
				'type': type1,
				'valid_till': valid_till,
			})
			to_email = form1.cleaned_data.get('email')
			phone_no = form1.cleaned_data.get('phone_no')
			email = EmailMessage(email_subject, message, to=[to_email])
			email.content_subtype = 'html'
			email.send()
			payload = {}
			payload['authkey'] = "95631AQvoigMsq5ec52866P1"
			payload['content-type'] = "application/json"
			payload['mobiles'] = phone_no
			payload['flow_id'] = "5efada07d6fc05445570a4f2"
			payload['ID'] = user.special_id
			print(payload)
			url = "https://api.msg91.com/api/v5/flow/"
			response = requests.post(url, json=payload)
			data = response.json()
			print("data", data)
			login(request, user)
			if request.user.is_authenticated:
				IndivdualDoctorProfile.objects.create(user=request.user)
			if next:
				return redirect(next)
			return redirect('profile_individual_doctor')
		else:
			email = request.POST.get('email')
			phone_no = request.POST.get('phone_no')
			if CustomUser.objects.filter(email=email).exists():
				return redirect('/register', messages.error(request, 'Email already Exists!', 'alert-danger'))
			elif CustomUser.objects.filter(phone_no=phone_no).exists():
				return redirect('/register', messages.error(request, 'Phone Number already Exists!', 'alert-danger'))
			else:
				return redirect('/register', messages.error(request, 'Form is not valid', 'alert-danger'))
	else:
		form1 = IndivdualDoctorForm(request.POST)

	if 'hospital' in request.POST:
		form2 = HospitalForm(request.POST)
		if form2.is_valid():
			user = form2.save(commit=False)
			password = form2.cleaned_data.get('password')
			# payment = request.POST.get('yesno')
			# user.payment = payment
			user.set_password(password)
			user.is_hdc_hospital = True
			user.save()
			email_subject = 'Welcome To Health Perigon!'
			valid_till = (datetime.datetime.now() + datetime.timedelta(days=364)).date()
			date = json.dumps(valid_till, indent=4, sort_keys=True, default=str)
			type1 = "HDC - Hospital"
			message = render_to_string('activate_account.html', {
				'user': user,
				'type': type1,
				'valid_till': valid_till,
			})
			to_email = form2.cleaned_data.get('email')
			phone_no = form2.cleaned_data.get('phone_no')
			email = EmailMessage(email_subject, message, to=[to_email])
			email.content_subtype = 'html'
			email.send()
			payload = {}
			payload['authkey'] = "95631AQvoigMsq5ec52866P1"
			payload['content-type'] = "application/json"
			payload['mobiles'] = phone_no
			payload['flow_id'] = "5efada07d6fc05445570a4f2"
			payload['ID'] = user.special_id
			print(payload)
			url = "https://api.msg91.com/api/v5/flow/"
			response = requests.post(url, json=payload)
			data = response.json()
			print("data", data)
			login(request, user)
			if request.user.is_authenticated:
				HospitalProfile.objects.create(user=request.user)
			if next:
				return redirect(next)
			return redirect('profile_hospital')
		else:
			email = request.POST.get('email')
			phone_no = request.POST.get('phone_no')
			if CustomUser.objects.filter(email=email).exists():
				return redirect('/register', messages.error(request, 'Email already Exists!', 'alert-danger'))
			elif CustomUser.objects.filter(phone_no=phone_no).exists():
				return redirect('/register', messages.error(request, 'Phone Number already Exists!', 'alert-danger'))
			else:
				return redirect('/register', messages.error(request, 'Form is not valid', 'alert-danger'))
	else:
		form2 = HospitalForm(request.POST)

	if 'nursinghome' in request.POST:
		form3 = NursingHomeForm(request.POST)
		if form3.is_valid():
			user = form3.save(commit=False)
			password = form3.cleaned_data.get('password')
			user.set_password(password)
			user.is_hdc_nursing_home = True
			user.save()
			email_subject = 'Welcome To Health Perigon!'
			valid_till = (datetime.datetime.now() + datetime.timedelta(days=364)).date()
			date = json.dumps(valid_till, indent=4, sort_keys=True, default=str)
			type1 = "HDC - Nursing Home"
			message = render_to_string('activate_account.html', {
				'user': user,
				'type': type1,
				'valid_till': valid_till,
			})
			to_email = form3.cleaned_data.get('email')
			phone_no = form3.cleaned_data.get('phone_no')
			email = EmailMessage(email_subject, message, to=[to_email])
			email.content_subtype = 'html'
			email.send()
			payload = {}
			payload['authkey'] = "95631AQvoigMsq5ec52866P1"
			payload['content-type'] = "application/json"
			payload['mobiles'] = phone_no
			payload['flow_id'] = "5efada07d6fc05445570a4f2"
			payload['ID'] = user.special_id
			print(payload)
			url = "https://api.msg91.com/api/v5/flow/"
			response = requests.post(url, json=payload)
			data = response.json()
			print("data", data)
			login(request, user)
			if request.user.is_authenticated:
				NursingHomeProfile.objects.create(user=request.user)
			if next:
				return redirect(next)
			return redirect('profile_nursing_home')
		else:
			email = request.POST.get('email')
			phone_no = request.POST.get('phone_no')
			if CustomUser.objects.filter(email=email).exists():
				return redirect('/register', messages.error(request, 'Email already Exists!', 'alert-danger'))
			elif CustomUser.objects.filter(phone_no=phone_no).exists():
				return redirect('/register', messages.error(request, 'Phone Number already Exists!', 'alert-danger'))
			else:
				return redirect('/register', messages.error(request, 'Form is not valid', 'alert-danger'))
	else:
		form3 = NursingHomeForm(request.POST)

	if 'individualuser' in request.POST:
		form = IndivdualUserForm(request.POST)
		print("POST")
		print(form.errors)
		if form.is_valid():
			user = form.save(commit=False)
			password = form.cleaned_data.get('password')
			user.set_password(password)
			user.is_individual = True
			user.save()
			email_subject = 'Welcome To Health Perigon!'
			valid_till = (datetime.datetime.now() + datetime.timedelta(days=364)).date()
			date = json.dumps(valid_till, indent=4, sort_keys=True, default=str)
			type1 = "HDC - Individual User"
			message = render_to_string('activate_account.html', {
				'user': user,
				'type': type1,
				'valid_till': valid_till,
			})
			to_email = form.cleaned_data.get('email')
			phone_no = form.cleaned_data.get('phone_no')
			email = EmailMessage(email_subject, message, to=[to_email])
			email.content_subtype = 'html'
			email.send()
			payload = {}
			payload['authkey'] = "95631AQvoigMsq5ec52866P1"
			payload['content-type'] = "application/json"
			payload['mobiles'] = phone_no
			payload['flow_id'] = "5efada07d6fc05445570a4f2"
			payload['ID'] = user.special_id
			print(payload)
			url = "https://api.msg91.com/api/v5/flow/"
			response = requests.post(url, json=payload)
			data = response.json()
			print("data", data)
			login(request, user)
			if request.user.is_authenticated:
				IndivdualUserProfile.objects.create(user=request.user)
			if next:
				return redirect(next)
			return redirect('profile_individual_user')
		else:
			email = request.POST.get('email')
			phone_no = request.POST.get('phone_no')
			if CustomUser.objects.filter(email=email).exists():
				return redirect('/register', messages.error(request, 'Email already Exists!', 'alert-danger'))
			elif CustomUser.objects.filter(phone_no=phone_no).exists():
				return redirect('/register', messages.error(request, 'Phone Number already Exists!', 'alert-danger'))
			else:
				return redirect('/register', messages.error(request, 'Form is not valid', 'alert-danger'))
	else:
		form = IndivdualUserForm()

	return render(request, "Register.html", {'form': form, 'form1': form1, 'form2': form2, 'form3': form3})


@superadmin_required
@csrf_exempt
def existing_module_master(request):
	if request.user.is_authenticated:
		# user = ModuleMaster.objects.get(user=request.user)
		# module = ModuleMaster.objects.filter(user=user.user)
		module = ModuleMaster.objects.all()
		return render(request, "Subscription_Master-Existing_Module_Master.html", {'module': module})


@superadmin_required
@csrf_exempt
def create_module_master(request):
	# user = ModuleMaster.objects.get(user=request.user)
	if request.method == 'POST':
		form = ModuleMasterForm(request.POST)
		if form.is_valid():
			# module_name = form.cleaned_data.get('module_name')
			# module_code = form.cleaned_data.get('module_code')
			# no_of_patients = form.cleaned_data.get('no_of_patients')
			# web_space = form.cleaned_data.get('web_space')
			# amount = form.cleaned_data.get('amount')
			# cgst = form.cleaned_data.get('cgst')
			# sgst = form.cleaned_data.get('sgst')
			# gst = form.cleaned_data.get('gst')
			# total_amount = form.cleaned_data.get('total_amount')
			# ModuleMaster.objects.create(user = request.user, module_name = module_name, module_code = module_code, no_of_patients = no_of_patients, web_space = web_space, amount = amount, cgst = cgst, sgst = sgst, gst = gst, total_amount = total_amount)
			# ModuleMaster.objects.create(user= request.user)
			if form.save():
				return redirect('/create_module_master', messages.success(request, 'Module is successfully created.', 'alert-success'))
			else:
				return redirect('/create_module_master', messages.error(request, 'Module is not saved', 'alert-danger'))
		else:
			return redirect('/create_module_master', messages.error(request, 'Form is not valid', 'alert-danger'))
	else:
		form = ModuleMasterForm()
		return render(request, 'Subscription_Master-Create_Module_Master.html', {'form': form})


@superadmin_required
@csrf_exempt
def edit_module_master(request, module_id):
    module = ModuleMaster.objects.get(id=module_id)
    if request.POST:
        form = ModuleMasterForm(request.POST, instance=module)
        if form.is_valid():
            if form.save():
                return redirect('/existing_module_master', messages.success(request, 'Module is successfully updated.', 'alert-success'))
            else:
                return redirect('/existing_module_master', messages.error(request, 'Module is not saved', 'alert-danger'))
        else:
            return redirect('/existing_module_master', messages.error(request, 'Form is not valid', 'alert-danger'))
    else:
        form = ModuleMasterForm(instance=module)
        return render(request, 'Subscription_Master-Edit_Module_Master.html', {'form': form})


@superadmin_required
@csrf_exempt
def destroy_module_master(request, module_id):
    module = ModuleMaster.objects.get(id=module_id)
    module.delete()
    return redirect('/existing_module_master', messages.success(request, 'Module is successfully deleted.', 'alert-success'))


@csrf_exempt
def password_reset(request):
	form = PasswordForm(request.POST or None)
	form1 = PasswordVerificationForm(request.POST or None)

	if request.method == 'POST':
		question = request.POST.get('question')
		answer = request.POST.get('answer')
		phone_no = request.POST.get('phone_no')
		print("question", question)
		print("answer", answer)
		print("phone_no", phone_no)
		# change it when adding security question
		check = SecurityQuestions.objects.get(id=1)
		print(check.answer)
		if check.answer == answer:
			data_json = {"error": False, "errorMessage": "Correct Answer"}
			return JsonResponse(data_json, safe=False)
		else:
			data_json = {"error": True, "errorMessage": "Incorrect Answer"}
			return JsonResponse(data_json, safe=False)
	else:
		form = PasswordForm()
		form1 = PasswordVerificationForm()
	return render(request, "forget_password.html", {"form": form, "form1": form1})


@csrf_exempt
def change_password(request):
	form = PasswordForm()
	if request.method == 'POST':
		print("dfdssgddddddddddddddddddddddddddddddddddddddddddddddddddddd")
		password = request.POST.get('password')
		password_confirm = request.POST.get('password_confirm')
		if password != password_confirm:
			print("mismatch")
			data_json = {"error": True, "errorMessage": "Password Mismatch"}
			return JsonResponse(data_json, safe=False)
		else:
			request.user.password = make_password(password)
			request.user.save()
			print("success")
			data_json = {"error": False, "errorMessage": "Password Changed"}
			return JsonResponse(data_json, safe=False)
	return render(request, "forget_password.html", {"form": form})


@csrf_exempt
def send_otp(request):
	if request.method == "GET":
		# url = "https://api.msg91.com/api/v5/otp?authkey=95631AQvoigMsq5ec52866P1&template_id=5ec52d2dd6fc050944666272&mobile=+919702221660&invisible=1&otp=OTP to send and verify. If not sent, OTP will be generated.&userip=IPV4 User IP&email=Email ID"
		url = "https://api.msg91.com/api/v5/otp?authkey=95631AQvoigMsq5ec52866P1&template_id=5ec52d2dd6fc050944666272&mobile=+919702221660&invisible=1&userip=IPV4 User IP&email=Email ID"
		response = requests.request("GET", url)
		data = response.json()
		print("data", data)
		data_json = {"error": False, "errorMessage": "OTP Sent to your phone"}
	else:
		data_json = {"error": True, "errorMessage": "Failed to send OTP"}
	return JsonResponse(data_json)


@csrf_exempt
def verify_otp(request):
	if request.method == "POST":
		otptxt = request.POST.get('phone_no')
		url = 'https://api.msg91.com/api/v5/otp/verify?mobile=+919702221660&otp=' + \
		    str(otptxt)+'&authkey=95631AQvoigMsq5ec52866P1'
		print(url)
		response = requests.request("POST", url)
		data = response.json()
		print("data", data)
		data_json = {"error": False, "errorMessage": "OTP verified"}
	else:
		data_json = {"error": True, "errorMessage": "Fail to verify"}
	return JsonResponse(data_json)


@csrf_exempt
def login_view(request):
	next = request.GET.get("next")
	check = CustomUser.objects.get(id=1)
	print("last login", check.last_login)
	if check.last_login != None:
		form = UserLoginForm(request.POST or None)
		if form.is_valid():
			print("form valided")
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if not user:
				print("first")
				return redirect('/accounts/login/', messages.error(request, 'Username or password is incorrect', 'alert-danger'))
			login(request, user)
			print("login done")
			if next:
				return redirect(next)
			if request.user.is_superuser:
				return redirect('existing_module_master')
			elif request.user.is_hdc_individual:
				return redirect('profile_individual_doctor')
			elif request.user.is_individual:
				return redirect('profile_individual_user')
			elif request.user.is_hdc_hospital:
				return redirect('profile_hospital')
			elif request.user.is_hdc_nursing_home:
				return redirect('profile_nursing_home')
		return render(request, "login.html", {'form': form})
	else:
		form = UserLoginForm(request.POST or None)
		form1 = SecurityQuestionsForm(request.POST or None)
		# print("length of form",form1)
		if form.is_valid() and form1.is_valid():
			form1.save()
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if not user:
				print("second")
				return redirect('/accounts/login/', messages.error(request, 'Username or password is incorrect', 'alert-danger'))
			login(request, user)
			if next:
				return redirect(next)
			return redirect('existing_module_master')
		return render(request, "login.html", {'form': form, 'form1': form1})


def logout_view(request):
	logout(request)
	return redirect('/')


@csrf_exempt
def addservice(request):
    if request.method == 'POST':
        reg = AddServices(request.POST)
        if reg.is_valid():
            if reg.save():
                return redirect('/addonservice', messages.success(request, 'Module is successfully updated.', 'alert-success'))
            else:
                return redirect('/addonservice', messages.error(request, 'Module is not saved', 'alert-danger'))
        else:
            return redirect('/addonservice', messages.error(request, 'Form is not valid', 'alert-danger'))
    else:
        reg = AddServices()
        return render(request, 'addservice.html', {'reg': reg})


@csrf_exempt
def addonservice(request):
    module = AddOnServices.objects.all()
    return render(request, "addservicetable.html", {'module': module})


@csrf_exempt
def destroyonservice(request, module_id):
    module = AddOnServices.objects.get(id=module_id)
    module.delete()
    return redirect('/addonservice', messages.success(request, 'Module is successfully deleted.', 'alert-success'))


@csrf_exempt
def pharmacytable(request):
	module = pharamcytab.objects.all()
	return render(request, 'pharmacytable.html', {'module': module})


@csrf_exempt
def pharmacy(request):
    if request.method == 'POST':
        reg = pharamcy(request.POST)

        print(reg.errors)
        if reg.is_valid():

            if reg.save():
                 return redirect('/pharmacytable', messages.success(request, 'Service is successfully updated.', 'alert-success'))
            else:
                return redirect('/pharmacytable', messages.error(request, 'Service not saved', 'alert-danger'))
        else:
            return redirect('/pharmacytable', messages.error(request, 'Service not valid', 'alert-danger'))
    else:
        reg = pharamcy()
        return render(request, 'pharmacy master.html', {'reg': reg})


@csrf_exempt
def destroypharamcy(request, module_id):
    module = pharamcytab.objects.get(id=module_id)
    module.delete()
    return redirect('/pharmacytable', messages.success(request, 'Module is successfully deleted.', 'alert-success'))


@csrf_exempt
def laboratory(request):
	if request.method == 'POST':
		rag = laboratorylab(request.POST)
		reg = labo(request.POST)
		data = reg.json()
		print("data", data)
		print(rag.errors)
		print(reg.errors)
		if rag.is_valid() and reg.is_valid():
			if rag.save() and reg.save():
				return redirect('/laboratorytable', messages.success(request, 'Form is successfully updated.', 'alert-success'))
			else:
				return redirect('/laboratorytable', messages.error(request, 'Form is not saved', 'alert-danger'))
		else:
			return redirect('/laboratorytable', messages.error(request, 'Form is not valid', 'alert-danger'))
	else:
	    rag = laboratorylab()
	    reg = labo()
	    return render(request, 'laboratory.html', {'rag': rag, 'reg': reg})


@csrf_exempt
def lob(request):
	module = Labour.objects.all()
	return render(request, 'laboratorytable.html', {'module': module})


@csrf_exempt
def labotable(request):
	module = Emptytext.objects.all()
	return render(request, 'laotable.html', {'module': module})


@csrf_exempt
def destroylaboratory(request, module_id):
	module = Labour.objects.get(id=module_id)
	module.delete()
	return redirect('/laboratorytable', messages.success(request, 'Module is successfully deleted.', 'alert-success'))


@csrf_exempt
def destroyemptytext(request, module_id):
	module = Emptytext.objects.get(id=module_id)
	module.delete()
	return redirect('/labotable', messages.success(request, 'Module is successfully deleted.', 'alert-success'))


@csrf_exempt
def edit_service(request, module_id):
    module1 = AddOnServices.objects.get(id=module_id)
    if request.POST:
        reg = AddServices(request.POST, instance=module1)
        if reg.is_valid():
            if reg.save():
                return redirect('/addservice', messages.success(request, 'Module is successfully updated.', 'alert-success'))
            else:
                return redirect('/addservice', messages.error(request, 'Module is not saved', 'alert-danger'))
        else:
            return redirect('/addservice', messages.error(request, 'Form is not valid', 'alert-danger'))
    else:
        reg = AddServices(instance=module1)
        return render(request, 'edit_service.html', {'reg': reg})


@csrf_exempt
def edit_pharmacy(request, module_id):
    module = pharamcytab.objects.get(id=module_id)
    if request.POST:
        reg = pharamcy(request.POST, instance=module)
        if reg.is_valid():
            if reg.save():
                return redirect('/pharmacy', messages.success(request, 'Module is successfully updated.', 'alert-success'))
            else:
                return redirect('/pharmacy', messages.error(request, 'Module is not saved', 'alert-danger'))
        else:
            return redirect('/pharmacy', messages.error(request, 'Form is not valid', 'alert-danger'))
    else:
        reg = pharamcy(instance=module)
        return render(request, 'edit_pharmacy.html', {'reg': reg})


@csrf_exempt
def edit_laboratorytable(request, module_id):
    module = Labour.objects.get(id=module_id)
    if request.POST:
        rag = laboratorylab(request.POST, instance=module)

        if rag.is_valid():
            if rag.save():
                return redirect('/laboratory', messages.success(request, 'Module is successfully updated.', 'alert-success'))
            else:
                return redirect('/laboratory', messages.error(request, 'Module is not saved', 'alert-danger'))
        else:
            return redirect('/laboratory', messages.error(request, 'Form is not valid', 'alert-danger'))
    else:
        rag = laboratorylab(instance=module)

        return render(request, 'edit_laboratorytable.html', {'rag': rag})


@csrf_exempt
def edit_labotable(request, module_id):
    module = Emptytext.objects.get(id=module_id)
    module = Labour.objects.get(id=module_id)
    if request.POST:
        rag = laboratorylab(request.POST, instance=module)
        reg = labo(request.POST, instance=module)

        if rag.is_valid() and reg.is_valid():
            if rag.save() and reg.is_valid():
                    return redirect('/lab)oratory', messages.success(request, 'Module is successfully updated.', 'alert-success'))
            else:
                return redirect('/laboratory', messages.error(request, 'Module is not saved', 'alert-danger'))
        else:
            return redirect('/laboratory', messages.error(request, 'Form is not valid', 'alert-danger'))
    else:
        rag = laboratorytable(instance=module)
        reg = labo(instance=module)

        return render(request, 'editlabour.html', {'reg': reg, 'rag': rag})


def update_database(request):
	reg = labo(request.POST or None)
	if request.method == 'POST':
		forms = request.POST.get('froms')
		to = request.POST.get('to')
		gender= request.POST.get('gender')
		umo1 = request.POST.get('umo1')
		umo2 = request.POST.get('umo2')
		conversationfactor = request.POST.get('conversationfactor')
		refrencerange = request.POST.get('conversationfactor')
		high = request.POST.get('high')
		return render(request,'sample2.html',{"reg":reg})
	else:
		reg= labo()
	return render(request,'sample2.html',{"reg":reg})
@csrf_exempt
def labo2(request):
	module = Empty.objects.all()
	return render(request,'sample.html',{'module':module})

def user_list(request):
	custmore_obj = CustomUser.objects.all()

	context = {
		'customers':custmore_obj

	}
	return render(request,'user_list.html',context)



def add_individual_user(request):
	if request.method == 'POST':
		form = IndivdualUserForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("../")
	else:
		form = IndivdualUserForm()
	return render(request,'add_user.html',{'form':form})

