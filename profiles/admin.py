from django.contrib import admin
from .models import IndivdualDoctorProfile,NursingHomeProfile,HospitalProfile,IndivdualUserProfile

# Register your models here.
admin.site.register(IndivdualDoctorProfile)
admin.site.register(NursingHomeProfile)
admin.site.register(HospitalProfile)
admin.site.register(IndivdualUserProfile)

