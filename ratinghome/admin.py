from django.contrib import admin
from unfold.admin import ModelAdmin  # Import the Unfold ModelAdmin
from .models import Rateinfo

@admin.register(Rateinfo)
class RateinfoAdmin(ModelAdmin):
    # Customize the list display
    list_display = ('pID', 'pName', 'province', 'culture', 'adventure', 'child_friendly')

    # Add search functionality
    search_fields = ('pName',)

    # Add filters
    list_filter = ('province', 'culture', 'adventure', 'wildlife', 'history', 'religious')

    # Customize the forms for JSONField
    fieldsets = (
        (None, {
            'fields': ('pID', 'pName', 'province')
        }),
        ('Categories', {
            'fields': ('culture', 'adventure', 'wildlife', 'sightseeing', 
                       'history', 'religious', 'child_friendly'),
            'classes': ('collapse',)  # Add collapsible sections for better UI
        }),
        ('Metadata', {
            'fields': ('tags', 'genre_bin', 'words_bin', 'params', 'genres'),
        }),
    )
