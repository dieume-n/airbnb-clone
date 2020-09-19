from django.db import models
from django_countries.fields import CountryField
from core import models as core_models
from users import models as user_models


class RoomType(core_models.AbstractItem):
    """ Room Type Model definition """
    class Meta:
        verbose_name = 'Room Type'


class Amenity(core_models.AbstractItem):
    """ Amenity Model definition """
    class Meta:
        verbose_name_plural = 'Amenities'


class Facility(core_models.AbstractItem):
    """ Facility Model definition """
    class Meta:
        verbose_name_plural = 'Facilities'


class HouseRule(core_models.AbstractItem):
    """ House Rules Model definition """
    class Meta:
        verbose_name = 'House Rule'


class Room(core_models.TimeStampedModel):
    """ Room Model definition """
    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    guests = models.IntegerField()
    address = models.CharField(max_length=140)
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey(user_models.User, related_name='rooms', on_delete=models.CASCADE)
    room_type = models.ForeignKey(RoomType, related_name='rooms', on_delete=models.SET_NULL, null=True)
    amenities = models.ManyToManyField(Amenity, blank=True)
    facilities = models.ManyToManyField(Facility, blank=True)
    house_rules = models.ManyToManyField(HouseRule, blank=True)

    def __str__(self):
        return self.name


class Photo(core_models.TimeStampedModel):
    """ Photo Model definition """
    caption = models.CharField(max_length=100)
    file = models.ImageField()
    room = models.ForeignKey(Room, related_name='photos', on_delete=models.CASCADE)

    def __str__(self):
        return self.caption
