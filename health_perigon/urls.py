from django.contrib import admin
from django.urls import path
from accounts.views import home, login_view, logout_view, contact, password_reset, contact_master, change_password, send_otp, verify_otp, existing_module_master, create_module_master, edit_module_master, destroy_module_master
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home, name="home"),
    path('contact/',contact, name="contact"),
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
]
