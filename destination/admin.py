from django.contrib import admin
from unfold.admin import ModelAdmin  # Use Unfold's ModelAdmin
from .models import Places, Place_rating, Comment, Destimages, Mf_result

@admin.register(Places)
class PlacesAdmin(ModelAdmin):
    list_display = ('name', 'address', 'ispopular', 'rateinfo')
    search_fields = ('name', 'address')
    list_filter = ('ispopular',)
    fieldsets = (
        (None, {
            'fields': ('name', 'address', 'descrption', 'ispopular')
        }),
        ('Image', {
            'fields': ('thumbnail_image',),
        }),
        ('Rate Info', {
            'fields': ('rateinfo',),
        }),
    )

@admin.register(Place_rating)
class PlaceRatingAdmin(ModelAdmin):
    list_display = ('place', 'user', 'rate')
    list_filter = ('rate',)
    search_fields = ('place__name', 'user__username')

@admin.register(Comment)
class CommentAdmin(ModelAdmin):
    list_display = ('place', 'user', 'created_date')
    list_filter = ('created_date',)
    search_fields = ('place__name', 'user__username', 'comment_body')

@admin.register(Destimages)
class DestimagesAdmin(ModelAdmin):
    list_display = ('place',)
    search_fields = ('place__name',)
    fieldsets = (
        (None, {
            'fields': ('place', 'image'),
        }),
    )

@admin.register(Mf_result)
class MfResultAdmin(ModelAdmin):
    list_display = ('place', 'user', 'rate')
    search_fields = ('place__name', 'user__username')
    list_filter = ('rate',)
