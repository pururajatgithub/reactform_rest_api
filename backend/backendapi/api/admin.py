from django.contrib import admin

from .models import User
# Register your models here.

class AdminUser(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone', 'email']


admin.site.register(User, AdminUser)