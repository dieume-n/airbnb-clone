from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    """ Custom User Model"""

    GENDER_MALE = 'male'
    GENDER_FEMALE = 'female'
    GENDER_OTHER = 'other'

    GENDER_CHOICES = (
        (GENDER_MALE, 'Male'),
        (GENDER_FEMALE, 'Female'),
        (GENDER_OTHER, 'Other')
    )

    LANGUAGE_ENGLISH = 'english'
    LANGUAGE_FRENCH = 'french'

    LANGUAGE_CHOICES = (
        (LANGUAGE_ENGLISH, 'English'),
        (LANGUAGE_FRENCH, 'French'),
    )

    CURRENCY_DOLLAR = 'usd'
    CURRENCY_SHILLING = 'ksh'
    CURRENCY_EURO = 'euro'

    CURRENCY_CHOICE = (
        (CURRENCY_DOLLAR, 'USD'),
        (CURRENCY_SHILLING, 'KSH'),
        (CURRENCY_EURO, 'EURO')
    )

    avatar = models.ImageField(null=True, blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, null=True)
    bio = models.TextField(default="", blank=True)
    date_of_birth = models.DateField(null=True)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=10, null=True, blank=True)
    currency = models.CharField(choices=CURRENCY_CHOICE, max_length=5, null=True, blank=True)
    is_superhost = models.BooleanField(default=False)
