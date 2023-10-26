from django.urls import path
from . import views

urlpatterns = [
    path('', views.review, name='review'),
    path('buku/<int:book_id>/', views.review, name='review-detail')
]
