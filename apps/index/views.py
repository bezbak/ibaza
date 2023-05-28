from rest_framework import generics
from apps.index.models import Reviews, Contact
from apps.index.serializers import ReviewsSerializer, ContactSerializer
# Create your views here.
class ReviewsAPIView(generics.ListAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer

class ContactAPIView(generics.ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
