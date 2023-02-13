from django.contrib import admin

from .models import Flat, Complaint, Owner


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
    raw_id_fields = ('like',)


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('user', 'complaint_flat',)


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    search_fields = ('owner', 'owner_pure_phone',)
    list_display = (
        'pk',
        'owner',
        'owners_phonenumber',
        'owner_pure_phone',
    )
    raw_id_fields = ('flats',)
