from django.contrib import admin
from .models import UserAccount
@admin.register(UserAccount)
class AdminUserAccount(admin.ModelAdmin):
    list_display = ['id','User_Name','User_Email','User_Password']