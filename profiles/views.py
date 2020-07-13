from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .forms import IndivdualDoctorProfileForm, UserForm, NursingHomeProfileForm, HospitalProfileForm, IndivdualUserProfileForm
from accounts.models import CustomUser
from .models import IndivdualDoctorProfile, NursingHomeProfile, HospitalProfile, IndivdualUserProfile
from accounts.decorators import individual_required, hdc_individual_required, hdc_hospital_required, hdc_nursing_home_required

@hdc_individual_required
@csrf_exempt
def individual_doctor(request):
	print("First ",request.user)
	if request.user.is_authenticated:
		user_profile = IndivdualDoctorProfile.objects.get(user=request.user)
	if request.POST:
		userform = UserForm(request.POST, instance = request.user)
		profileform = IndivdualDoctorProfileForm(request.POST,request.FILES, instance = user_profile)
		print(userform.errors, profileform.errors)
		if userform.is_valid() and profileform.is_valid():
			user = userform.save()
			profile = profileform.save(commit=False)
			profile.user = user

		if 'picture' in request.FILES:
			print("PICTURE ",request.FILES['picture'])
			profile.picture = request.FILES['picture']
			profile.save()

			return redirect('/profile_individual_doctor', messages.success(request, 'Profile Successfully Updated.', 'alert-success'))
		else:
			#print(userform.errors, profileform.errors)
			return redirect('/profile_individual_doctor', messages.error(request, 'Profile is not Valid', 'alert-danger'))
	else:
		form1 = UserForm(instance = request.user)
		form2 = IndivdualDoctorProfileForm(instance = user_profile)
	return render(request,'Profile_HDC_Individual_Doctor.html', {'form1':form1, 'form2': form2})

@individual_required
@csrf_exempt
def individual_user(request):
	print("First ",request.user)
	if request.user.is_authenticated:
		user_profile = IndivdualUserProfile.objects.get(user=request.user)
	if request.POST:
		userform = UserForm(request.POST, instance = request.user)
		profileform = IndivdualUserProfileForm(request.POST, instance = user_profile)
		print(userform.errors, profileform.errors)
		if userform.is_valid() and profileform.is_valid():
			user = userform.save(commit=False)
			user.save()
			profile = profileform.save(commit=False)
			profile.user = user
			profile.save()

			return redirect('/profile_individual_user', messages.success(request, 'Profile Successfully Updated.', 'alert-success'))
		else:
			#print(userform.errors, profileform.errors)
			return redirect('/profile_individual_user', messages.error(request, 'Profile is not Valid', 'alert-danger'))
	else:
		form1 = UserForm(instance = request.user)
		form2 = IndivdualUserProfileForm(instance = user_profile)
	return render(request, "Profile_Individual.html", {'form1':form1, 'form2': form2})

@hdc_hospital_required
@csrf_exempt
def hospital(request):
	print("First ",request.user)
	if request.user.is_authenticated:
		user_profile = HospitalProfile.objects.get(user=request.user)
	if request.POST:
		userform = UserForm(request.POST, instance = request.user)
		profileform = HospitalProfileForm(request.POST,request.FILES, instance = user_profile)
		print(userform.errors, profileform.errors)
		if userform.is_valid() and profileform.is_valid():
			user = userform.save()
			profile = profileform.save(commit=False)
			profile.user = user

		if 'picture' in request.FILES:
			print("PICTURE ",request.FILES['picture'])
			profile.picture = request.FILES['picture']
			profile.save()

			return redirect('/profile_hospital', messages.success(request, 'Profile Successfully Updated.', 'alert-success'))
		else:
			#print(userform.errors, profileform.errors)
			return redirect('/profile_hospital', messages.error(request, 'Profile is not Valid', 'alert-danger'))
	else:
		form1 = UserForm(instance = request.user)
		form2 = HospitalProfileForm(instance = user_profile)
	return render(request, "Profile_HDC_Hospital.html", {'form1':form1, 'form2': form2})

@hdc_nursing_home_required
@csrf_exempt
def nursing_home(request):
	print("First ",request.user)
	if request.user.is_authenticated:
		user_profile = NursingHomeProfile.objects.get(user=request.user)
	if request.POST:
		userform = UserForm(request.POST, instance = request.user)
		profileform = NursingHomeProfileForm(request.POST,request.FILES, instance = user_profile)
		print(userform.errors, profileform.errors)
		if userform.is_valid() and profileform.is_valid():
			user = userform.save()
			profile = profileform.save(commit=False)
			profile.user = user

		if 'picture' in request.FILES:
			print("PICTURE ",request.FILES['picture'])
			profile.picture = request.FILES['picture']
			profile.save()

			return redirect('/profile_nursing_home', messages.success(request, 'Profile Successfully Updated.', 'alert-success'))
		else:
			#print(userform.errors, profileform.errors)
			return redirect('/profile_nursing_home', messages.error(request, 'Profile is not Valid', 'alert-danger'))
	else:
		form1 = UserForm(instance = request.user)
		form2 = NursingHomeProfileForm(instance = user_profile)
	return render(request, "Profile_HDC_Nursing_Home.html", {'form1':form1, 'form2': form2})

