from django.urls import path
from . import views
app_name = "review_buku"

urlpatterns = [
    path('review/<int:id>/', views.review, name='review'),  # Tambahkan id sebagai parameter
    path('show/<int:id>/', views.show_reviews, name='show_reviews'),  # Tambahkan id sebagai parameter
    path('post_review/', views.post_review, name='post_review'),
]

