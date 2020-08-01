from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from accounts.views import Coupon_to_create,add_coupon,Coupon_status_change,coupon_code_list,account_status_change,individual_doctor_user_list,home, login_view, logout_view, contact, activate_account, register, password_reset, contact_master, change_password, send_otp, verify_otp, existing_module_master, create_module_master, edit_module_master, destroy_module_master, addservice,addonservice,destroyonservice,pharmacy,pharmacytable,laboratory,lob,destroypharamcy,labotable,destroylaboratory,destroyemptytext,edit_laboratorytable,edit_service,edit_pharmacy,edit_labotable,update_database,labo2,user_list,add_individual_user,User_creation
from profiles.views import individual_doctor, individual_user, nursing_home, hospital     #AddCoupon,
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home, name="home"),
    path('contact/',contact, name="contact"),
    path('register/',register, name="register"),
    path('contact_master/',contact_master, name="contact_master"),
    path('existing_module_master/',existing_module_master, name="existing_module_master"),
    path('create_module_master/',create_module_master, name="create_module_master"),
    path('edit_module_master/<int:module_id>',edit_module_master, name="edit_module_master"),
    path('destroy_module_master/<int:module_id>',destroy_module_master, name="destroy_module_master"),
    path('password_reset/',password_reset, name="password_reset"),
    path('change_password/',change_password, name="change_password"),
    path('accounts/login/',login_view, name="login_view"),
    path('accounts/logout/',logout_view, name="logout_view"),
    path('send_otp/',send_otp, name="send_otp"),
    path('verify_otp/',verify_otp, name="verify_otp"),
    path('addservice/',addservice,name="addservice"),
    path('addonservice/',addonservice,name="addonservice"),
    path('destroyonservice/<int:module_id>',destroyonservice,name="destroyonservice"),
    path('pharmacy/',pharmacy,name="pharmacy"),
    path('pharmacytable/',pharmacytable,name="pharmacytable"),
    path('laboratory/',laboratory,name="laboratory"),
    path('laboratorytable/',lob,name="laboratorytable"),
    path('destroypharamcy/<int:module_id>',destroypharamcy,name="destroypharamcy"),
    path('labotable/',labotable,name="labotable"),
    path('destroylaboratory/<int:module_id>',destroylaboratory,name="destroylaboratory"),
    path('destroyemptytext/<int:module_id>',destroyemptytext,name="destroyemptytext"),
    path('edit_laboratorytable/<int:Labour>',edit_laboratorytable, name="edit_laboratorytable"),
    path('edit_pharmacy/<int:module_id>',edit_pharmacy, name="edit_pharmacy"),
    path('edit_service/<int:module_id>',edit_service, name="edit_service"),
    path('update_database/',update_database ,name="update_database"),
    path('labo2/',labo2 ,name="labo2"),

    path('profile_individual_doctor/',individual_doctor, name="profile_individual_doctor"),
    path('profile_individual_user/',individual_user, name="profile_individual_user"),
    path('profile_hospital/',hospital, name="profile_hospital"),
    path('profile_nursing_home/',nursing_home, name="profile_nursing_home"),


    path('add_individual_user/',add_individual_user,name='add_individual_user'),
    path('User_creation/',User_creation,name='User_creation'),
    path('individual_doctor_user_list/',individual_doctor_user_list,name='individual_doctor_user_list'),

    path('user_list/', user_list, name='user_list'),
    path('account_status_change/',account_status_change,name='account_status_change'),
    path('coupon_code_list/',coupon_code_list,name='coupon_code_list'),
    path('Coupon_status_change/',Coupon_status_change,name='Coupon_status_change'),
    # path('AddCoupon/',AddCoupon.as_view(),name='AddCoupon'),

    path('add_coupon/',add_coupon,name='add_coupon'),
    path('Coupon_to_create',Coupon_to_create,name='Coupon_to_create')


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
