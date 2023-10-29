from django.contrib import admin
from .models import Review

# Register your models here.
@admin.register(Review)
class Review(admin.ModelAdmin):
    list_display = ('buku', 'review_text')
