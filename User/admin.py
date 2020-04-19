from django.contrib import admin
from .models import User
from .models import NewsUsers

# Register your models here.
from django.contrib.auth.admin import UserAdmin
#admin.site.register(User, UserAdmin)

class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('email', 'date_added',)
admin.site.register(NewsUsers, SubscriptionAdmin)

class UserAdmin(UserAdmin):
   model = User
   list_display = ['username','email', 'first_name', 'last_name', 'user_type' ,'is_staff', ]
admin.site.register(User, UserAdmin)

