from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Complaint, CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser

    list_display = ['username', 'email', 'role', 'department', 'is_staff']
    list_filter = ['role', 'department', 'is_staff']

    fieldsets = UserAdmin.fieldsets + (
        ('Extra Info', {'fields': ('role', 'department')}),  # <-- tuple here
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Extra Info', {'fields': ('role', 'department')}),  # <-- and here
    )
admin.site.register(Complaint)


