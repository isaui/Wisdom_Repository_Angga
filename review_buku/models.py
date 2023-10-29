from django.contrib.auth.models import User
from django.db import models
from django.conf import settings

class Buku(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Review(models.Model):
    buku = models.ForeignKey(Buku, on_delete=models.CASCADE, related_name='reviews')
    review_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

# class Buku(models.Model):
#     judul = models.CharField(max_length=100)
#     gambar = models.CharField(max_length=100)
#     penulis = models.CharField(max_length=100)
#     user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
#     rating = models.FloatField()
#     tahun = models.IntegerField()
#     returned = models.BooleanField(default=False)
#     borrow_date = models.DateField(null=True, blank=True)
#     return_date = models.DateField(null=True, blank=True)
    
#     def __str__(self):
#         return self.judul

#     def __unicode__(self):
#         return self.judul
