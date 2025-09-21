from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm



class CustomUserAdmin(UserAdmin):
    model : CustomUser
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ('username', 'first_name', 'last_name', 'email')
    fieldsets = (
        ("Authentication", {"fields": ("username", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name", "email")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "first_name", "last_name", "email", "password1", "password2", "is_staff", "is_active"),
        }),
    )


admin.site.register(CustomUser,CustomUserAdmin)
