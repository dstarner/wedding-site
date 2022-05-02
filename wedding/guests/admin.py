import csv
from django.contrib import admin
from django.http import HttpResponse

from .models import Party, Guest


class ExportCsvMixin:

    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields] + getattr(self, 'related_csv_fields', [])

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export Selected"




class GuestAdmin(admin.StackedInline):

    model = Guest
    extra = 0


@admin.register(Party)
class PartyAdmin(admin.ModelAdmin, ExportCsvMixin):
    icon_name = 'group_add'
    actions = ["export_as_csv"]

    fieldsets = (
        (None, {
            'fields': ('name', 'type', 'code', 'side', 'association'),
        }),
        ('Wedding Involvement', {
            'fields': ('tier', 'guests_allowed', 'is_invited', 'rehearsal_dinner'),
        }),
        ('Contact Information', {
            'fields': ('contact_method', 'address', 'second_address', 'phone'),
        }),
        ('Logistics', {
            'fields': ('save_the_date_sent', 'invitation_sent', 'is_attending', 'comments'),
        }),
    )
    list_filter = (
        'type', 'tier', 'association', 'side', 'save_the_date_sent', 'invitation_sent',
        'is_invited', 'is_attending', 'rehearsal_dinner', 'contact_method',
    )
    list_display = ('full_name', 'guests_allowed', 'association', 'tier', 'side', 'is_invited', 'is_attending')
    inlines = [GuestAdmin]
    readonly_fields = ('code', 'is_attending', 'comments')
    search_fields = ('name',)


@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin, ExportCsvMixin):
    icon_name = 'how_to_reg'
    actions = ["export_as_csv"]

    list_display = ('first_name', 'last_name', 'party')
    search_fields = ('last_name', 'first_name', 'party__name')
    list_filter = ('role', 'is_child')
    related_csv_fields = ['address', 'second_address']
