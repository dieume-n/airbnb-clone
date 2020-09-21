from django.contrib import admin
from django.utils.html import mark_safe
from . import models


@admin.register(models.RoomType, models.Amenity, models.Facility, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):
    """ Item Admin definition """
    list_display = ('name', 'used_by')

    def used_by(self, obj):
        return obj.rooms.count()


class PhotoInline(admin.TabularInline):
    model = models.Photo

@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    """ Room Admin definition """
    inlines = (PhotoInline,)

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
            {"fields": ("guests", "bedrooms", "beds", "baths")}
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
                    'instant_book', 'count_amenities', 'count_photos', 'total_rating')
    ordering = ('price', 'bedrooms')
    raw_id_fields = ('host',)
    list_filter = ('instant_book', 'host__is_superhost', 'room_type', 'amenities', 'facilities', 'house_rules', 'city',
                   'country')
    search_fields = ("=city", "^host__username")
    filter_horizontal = ("amenities", "facilities", "house_rules")

    def count_amenities(self, obj):
        return obj.amenities.count()

    def count_photos(self, obj):
        return obj.photos.count()

    count_amenities.short_description = "# of amenities"
    count_photos.short_description = "# of photos"


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """ Photo Admin definition """
    list_display = ('__str__', 'get_thumbnail')

    def get_thumbnail(self, obj):
        return mark_safe(f'<a href="{obj.file.url}" target="_blank">Click to see</a>')

    get_thumbnail.short_description = "Thumbnail"

