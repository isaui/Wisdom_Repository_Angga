from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from daftar_buku.models import Buku

class Review(models.Model):
    buku = models.ForeignKey(Buku, on_delete=models.CASCADE, related_name='reviews')
    review_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)