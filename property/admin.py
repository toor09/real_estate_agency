from django.contrib import admin

from .models import Complaint, Flat, Owner


class FlatsInline(admin.TabularInline):
    model = Owner.flats.through
    raw_id_fields = ('owner', 'flat')


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'address',
        'price',
        'new_building',
        'construction_year',
        'town',
    )
    inlines = [
        FlatsInline
    ]
    list_editable = ('new_building',)
    list_filter = ('new_building', 'has_balcony', 'rooms_number',)
    search_fields = ('pk', 'town', 'address',)
    readonly_fields = ('created_at',)
    raw_id_fields = ('likes',)
    list_per_page = 250


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('user', 'complaint_flat',)


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    search_fields = ('full_name', 'formatted_phone',)
    list_display = (
        'pk',
        'full_name',
        'phone',
        'formatted_phone',
    )
    raw_id_fields = ('flats',)
