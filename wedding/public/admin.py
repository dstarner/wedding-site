from django.contrib import admin

from .models import GalleryItem, PlaceOfInterest, RegistryOrganization, TimelineEntry


@admin.register(TimelineEntry)
class TimelineEntryAdmin(admin.ModelAdmin):

    icon_name = 'timeline'
    list_display = ('title',)


@admin.register(GalleryItem)
class GalleryItemAdmin(admin.ModelAdmin):

    icon_name = 'insert_photo'
    list_display = ('title', 'picture')
    readonly_fields = ('thumbnail',)


@admin.register(RegistryOrganization)
class RegistryOrganizationAdmin(admin.ModelAdmin):
    icon_name = 'store'
    list_display = ('title', 'link',)


@admin.register(PlaceOfInterest)
class PlaceOfInterestAdmin(admin.ModelAdmin):
    icon_name = 'room'
    list_display = ('name', 'type')