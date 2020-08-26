from django.db import models


class TimeStampedModel(models.Model):
    """ Time stamped Model definition """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class AbstractItem(TimeStampedModel):
    """ Abstract Item Model definition """
    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name
