from django.contrib import admin

from .models import Party, Guest


class GuestAdmin(admin.StackedInline):

    model = Guest
    extra = 0


@admin.register(Party)
class PartyAdmin(admin.ModelAdmin):
    icon_name = 'group_add'
    fieldsets = (
        (None, {
            'fields': ('name', 'type', 'side', 'association'),
        }),
        ('Wedding Involvement', {
            'fields': ('tier', 'guests_allowed', 'is_invited', 'rehearsal_dinner'),
        }),
        ('Contact Information', {
            'fields': ('contact_method', 'address', 'email', 'phone'),
        }),
        ('Responses', {
            'fields': ('is_attending', 'comments'),
        }),
    )
    list_filter = ('tier', 'side', 'is_invited', 'rehearsal_dinner', 'contact_method', 'is_attending')
    list_display = ('full_name', 'guests_allowed', 'tier', 'side', 'is_invited', 'is_attending')
    inlines = [GuestAdmin]
    readonly_fields = ('is_attending', 'comments')
    search_fields = ('name',)


@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    icon_name = 'how_to_reg'

    list_display = ('first_name', 'last_name', 'party')
    search_fields = ('last_name', 'first_name', 'party__name')
    list_filter = ('role', 'is_child')