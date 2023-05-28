from django.urls import path
from apps.index.views import ReviewsAPIView, ContactAPIView

urlpatterns = [
    path('', ReviewsAPIView.as_view()),
    path('contact/', ContactAPIView.as_view()),
]