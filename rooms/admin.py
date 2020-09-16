from django.contrib import admin
from . import models


@admin.register(models.RoomType, models.Amenity, models.Facility, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):
    """ Item Admin definition """
    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    """ Room Admin definition """

    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "description", "country", "address", "price")}
        ),
        (
            "Times",
            {"fields": ("check_in", "check_out", "instant_book")}
        ),
        (
            "Spaces",
            {"fields": ("guests", "bedrooms", "baths")}
        ),
        (
            "More About the Space",
            {"fields": ("amenities", "facilities", "house_rules")}
        ),
        (
            "Last Details",
            {"fields": ("host",)}
        )
    )
    list_display = ('name', 'country', 'city', 'price', 'guests', 'beds', 'bedrooms', 'baths', 'check_in', 'check_out',
                    'instant_book')

    list_filter = ('instant_book', 'host__is_superhost', 'room_type', 'amenities', 'facilities', 'house_rules', 'city', 'country')
    search_fields = ("=city", "^host__username")
    filter_horizontal = ("amenities", "facilities", "house_rules")


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """ Photo Admin definition """
    pass
