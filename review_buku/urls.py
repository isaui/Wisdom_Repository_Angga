from django.urls import path
from . import views

urlpatterns = [
    path('', views.review, name='review'),
    path('buku/<int:book_id>/', views.review, name='review-detail'),
    path('postReview/', views.post_review, name='post_review'),
]
