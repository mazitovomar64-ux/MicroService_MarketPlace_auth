from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField



class UserProfile(AbstractUser):
    age = models.PositiveSmallIntegerField(null=True, blank=True,
                                           validators=[MinValueValidator(16), MaxValueValidator(70)])
    phone_number = PhoneNumberField(null=True, blank=True)
    avatar = models.ImageField(upload_to='user_images/')
    STATUS_CHOICES = (
        ('client', 'client'),
        ('owner', 'owner')
    )
    status = models.CharField(choices=STATUS_CHOICES, max_length=16, default='client')
    registered_data = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.username}, {self.status}'
