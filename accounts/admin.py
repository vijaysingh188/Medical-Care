from django.contrib import admin
from .models import CustomUser,SecurityQuestions,ModuleMaster,Contact,AddOnServices,Emptytext,pharamcytab,Labour,Empty,Coupon

class CouponAdmin(admin.ModelAdmin):
    list_display = ['code','startDate','endDate','count_value','active']
    list_filter = ['startDate','endDate','count_value','active']
    search_fields = ['code']



# Register your models here.
admin.site.register(SecurityQuestions)
admin.site.register(ModuleMaster)
admin.site.register(Contact)
admin.site.register(AddOnServices)
admin.site.register(Emptytext)
admin.site.register(pharamcytab)
admin.site.register(Labour)
admin.site.register(Empty)
admin.site.register(CustomUser)
admin.site.register(Coupon,CouponAdmin)

