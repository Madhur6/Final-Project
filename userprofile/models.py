from django.db import models
from django_countries.fields import CountryField
from core.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    name = models.CharField(max_length=100, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    about = models.TextField(max_length=225, blank=True, null=True)
    country = CountryField(blank=True, null=True)
    image = models.ImageField(default='profile_pictures/default-user.png', upload_to='profile_pictures')

    def __str__(self):
        return f"{self.user.username}"
