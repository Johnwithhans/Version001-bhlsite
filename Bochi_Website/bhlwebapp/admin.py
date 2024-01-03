# admin.py
from django.contrib import admin
from .models import Event, GalleryImage


admin.site.register(Event)


class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('description', 'image',)
    search_fields = ('description',)

admin.site.register(GalleryImage, GalleryImageAdmin)