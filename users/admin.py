
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

class CustomUserAdmin(UserAdmin):
    pass  # You can customize the user admin here if needed

admin.site.unregister(User)  # Unregister the default User admin
admin.site.register(User, CustomUserAdmin)  # Register the User model with your custom admin class
