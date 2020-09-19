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

    list_filter = UserAdmin.list_filter + ('is_superhost',)

    list_display = ('username', 'first_name', 'last_name', 'email', 'language',  'currency', 'is_active', 'is_superhost', 'is_staff',
                    'is_superuser')
