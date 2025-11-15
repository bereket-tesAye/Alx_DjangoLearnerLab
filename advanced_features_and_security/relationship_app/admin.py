from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django import forms

from .models import CustomUser


class CustomUserCreationForm(forms.ModelForm):
    """
    Form used in the admin for creating new users.
    Includes only the fields we want admins to fill in.
    """
    class Meta:
        model = CustomUser
        fields = ("email", "date_of_birth", "profile_photo")


class CustomUserChangeForm(forms.ModelForm):
    """
    Form used in the admin for editing existing users.
    """
    class Meta:
        model = CustomUser
        fields = ("email", "date_of_birth", "profile_photo", "is_active", "is_staff", "is_superuser")


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    # What to show in admin user list table
    list_display = ("email", "date_of_birth", "is_staff", "is_active")
    list_filter = ("is_staff", "is_active")

    # Editing an existing user
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal Info", {"fields": ("date_of_birth", "profile_photo")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Important Dates", {"fields": ("last_login",)}),
    )

    # Creating a new user form layout
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "date_of_birth", "profile_photo", "password1", "password2", "is_staff", "is_active"),
        }),
    )

    # Tell admin which field is the login field
    ordering = ("email",)
    search_fields = ("email",)


admin.site.register(CustomUser, CustomUserAdmin)
