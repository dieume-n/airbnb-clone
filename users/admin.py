from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    """ Custom User Admin """
    fieldsets = UserAdmin.fieldsets + (
        (
            'Custom Profile',
            {
                'fields': (
                    'avatar',
                    'gender',
                    'date_of_birth',
                    'bio',
                    'language',
                    'currency',
                    'is_superhost'
                )
            }
        ),
    )
    pass
