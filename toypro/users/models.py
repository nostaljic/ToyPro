from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """Default user for toyPro."""
    GENDER_SELECT= [
        ('M','Male'),#사용자 Male로 보여짐, DB M으로 저장
        ('F','Female'),
        ('C','Custom')
    ]

    #: First and last name do not cover name patterns around the globe
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    user_name = models.CharField(_("Alias of User"), blank=True, max_length=255)
    profile_picture = models.ImageField(blank =True)
    website= models.URLField(_("website"), max_length=200)
    bio = models.TextField(blank=True)
    email_address= models.CharField(_("Email"), blank=True, max_length=255)
    phone_number= models.CharField(_("Phone"), blank=True, max_length=255)
    gender = models.CharField(_("Gender"),blank=True, choices=GENDER_SELECT,max_length=255)
    followers = models.ManyToManyField("self")
    following = models.ManyToManyField("self")
    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})
