from django.contrib import admin
from .models import userProfile
# Register your models here.
@admin.register(userProfile)

class adminUser(admin.ModelAdmin):
    list_display=('id' , 'name' , 'email', 'password')