from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _
from .models import User, Role

# Register your models here.
@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    '''Admin View for Role'''

    list_display = ('description',)
    # list_filter = ('',)
    # inlines = [
    #     Inline,
    # ]
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    # search_fields = ('',)
    # date_hierarchy = ''
    # ordering = ('',)

class UserAdmin(BaseUserAdmin):
    '''Admin View for User'''

    list_display = ('email','get_full_name', 'is_active', 'is_staff')
    # list_filter = ('',)
    # inlines = [
    #     Inline,
    # ]
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    # search_fields = ('',)
    # date_hierarchy = ''
    ordering = ('id',)
    fieldsets = (
        (None, {
            'fields': (
                'email', 'password'
            ),
        }),
        (_('Personal Info'), {
            'fields': (
                'name', 'last_name', 'date_to_birth', 'profile_img'
            ),
        }),
        (_('Permisions'), {
            'fields': (
                'role', 'is_active', 'is_staff', 'is_superuser'
            ),
        }),
        (_('Important Dates'), {
            'fields': (
                'last_login',
            ),
        }),
        
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'role'),
        }),
    )

admin.site.register(User, UserAdmin)