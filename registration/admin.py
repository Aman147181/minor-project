from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Preferences, Profile

@admin.register(Preferences)
class PreferencesAdmin(ModelAdmin):
    list_display = ('user', 'culture', 'wildlife', 'adventure', 'sightseeing', 
                    'history', 'religious', 'child_friendly')
    search_fields = ('user__username',)
    list_filter = ('culture', 'wildlife', 'adventure', 'sightseeing', 
                   'history', 'religious', 'child_friendly')
    fieldsets = (
        (None, {
            'fields': ('user',)
        }),
        ('Preferences', {
            'fields': ('culture', 'wildlife', 'adventure', 'sightseeing', 
                       'history', 'religious', 'child_friendly'),
            'classes': ('collapse',)  # Optional collapsible section
        }),
    )

@admin.register(Profile)
class ProfileAdmin(ModelAdmin):
    list_display = ('user', 'sex', 'age', 'phone_number', 'nationality')
    search_fields = ('user__username', 'phone_number', 'nationality')
    list_filter = ('sex', 'nationality')
    fieldsets = (
        (None, {
            'fields': ('user', 'middle_name', 'sex', 'age', 'phone_number', 'nationality')
        }),
        ('Profile Picture', {
            'fields': ('profile_pic',),
        }),
    )
