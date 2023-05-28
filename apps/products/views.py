from rest_framework import generics
from apps.products.models import  Product, ProductRec, Exclusives, Order,OnlineCalc, InstallmentPlan
from apps.products.serializers import ProductSerializer, ProductRecSerializer, ExclusivesSerializer, OrderSerializer, OnlineCalcSerializer, InstallmentPlanSerializer
# Create your views here.
class ProductAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class ProductRecCreateAPIView(generics.CreateAPIView):
    queryset = ProductRec.objects.all()
    serializer_class = ProductRecSerializer
    
class ExclusivesCreateAPIView(generics.CreateAPIView):
    queryset = Exclusives.objects.all()
    serializer_class = ExclusivesSerializer
    
class OrderCreateAPIView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OnlineCalcCreateAPIView(generics.CreateAPIView):
    queryset = OnlineCalc.objects.all()
    serializer_class = OnlineCalcSerializer
    
class InstallmentPlanCreateAPIView(generics.CreateAPIView):
    queryset = OnlineCalc.objects.all()
    serializer_class = InstallmentPlanSerializer