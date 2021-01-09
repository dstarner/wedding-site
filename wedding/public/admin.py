from django.contrib import admin

from .models import GalleryItem, RegistryOrganization, TimelineEntry


@admin.register(TimelineEntry)
class TimelineEntryAdmin(admin.ModelAdmin):

    icon_name = 'timeline'
    list_display = ('title',)


@admin.register(GalleryItem)
class GalleryItem(admin.ModelAdmin):

    icon_name = 'insert_photo'
    list_display = ('title', 'picture')
    readonly_fields = ('thumbnail',)


@admin.register(RegistryOrganization)
class RegistryOrganization(admin.ModelAdmin):
    icon_name = 'store'
    list_display = ('link',)