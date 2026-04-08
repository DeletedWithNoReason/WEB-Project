from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'phone', 'role')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'phone', 'role')

class CustomUserAdmin(BaseUserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

    list_display = ('email', 'phone', 'role', 'is_staff', 'is_active')
    list_filter = ('role', 'is_staff', 'is_active')

    
    fieldsets = (
        (None, {'fields': ('email', 'phone', 'password')}),
        ('User Info', {'fields': ('role',)}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser', 'is_active')}),
    )

    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            
            'fields': ('email', 'phone', 'role', 'password1', 'password2'),
        }),
    )

    search_fields = ('email', 'phone')
    ordering = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)