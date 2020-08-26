from django.contrib import admin
from . import models


@admin.register(models.RoomType, models.Amenity, models.Facility, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):
    """ Item Admin definition """
    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    """ Room Admin definition """
    pass


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """ Photo Admin definition """
    pass

