from django.db import models
from core import models as core_models


class Review(core_models.TimeStampedModel):
    """ Review Model definition """
    review = models.TextField()
    accuracy = models.IntegerField()
    communication = models.IntegerField()
    cleanliness = models.IntegerField()
    location = models.IntegerField()
    check_in = models.IntegerField()
    value = models.IntegerField()
    user = models.ForeignKey('users.User', related_name='reviews', on_delete=models.CASCADE)
    room = models.ForeignKey('rooms.Room', related_name='reviews', on_delete=models.CASCADE)

    def rating_average(self):
        ratings = [self.accuracy, self.communication, self.cleanliness, self.location, self.check_in, self.value]
        average = sum(ratings) / len(ratings)
        return round(average, 2)

    def __str__(self):
        return f'{self.review} => {self.room}'
