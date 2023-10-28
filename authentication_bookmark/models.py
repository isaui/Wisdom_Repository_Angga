from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group, Permission
from django.db import models
from daftar_buku.models import Buku

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
    buku = models.ForeignKey(Buku, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)