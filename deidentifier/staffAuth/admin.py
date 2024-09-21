from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import StaffAuth, StaffAdmin

from .models import StaffAuth, SupervisorRelationship, StaffAdmin


class CustomStaffAuth(UserAdmin):
    model = StaffAuth
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('full_name',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',)}),
        ('Important dates', {'fields': ('data_created',)}),
    )

    add_fieldsets = (
            (None, {
                'classes': ('wide',),
                'fields': ('full_name','email' , ('password1', 'password2'),'is_supervisor','data_created'),
            }),
    )
    filter_horizontal=[]
    ordering=('full_name',)  # Use valid fields for ordering
    # Use valid fields for list_display
    list_display=('full_name', 'is_supervisor', 'email',)
    list_filter=('is_supervisor',)  # Use valid fields for list_filter

# Register your models here.
admin.site.register(StaffAdmin)
admin.site.register(StaffAuth, CustomStaffAuth)
admin.site.register(SupervisorRelationship)
