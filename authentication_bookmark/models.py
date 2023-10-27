from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    member = models.CharField(
        max_length=20,
        choices=[
            ('regular', 'Regular'),
            ('premium', 'Premium')
        ],
        default='regular'
    )

    groups = models.ManyToManyField(Group, related_name='custom_users_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_users_permissions')


class Bookmark(models.Model):
    buku = models.CharField(max_length=255)
    gambar = models.CharField(max_length=100)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)