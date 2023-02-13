from django.contrib import admin

from .models import Flat, Complaint, Owner


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    list_display = (
        'address',
        'price',
        'new_building',
        'construction_year',
        'town',
        'owners_phonenumber',
        'owner_pure_phone',
    )
    list_editable = ('new_building',)
    list_filter = ('new_building', 'has_balcony', 'rooms_number',)
    search_fields = ('town', 'address', 'owner',)
    readonly_fields = ('created_at',)
    raw_id_fields = ('like',)


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('user', 'complaint_flat',)


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('flats',)
