from rest_framework import serializers
from apps.products.models import  Product, ProductRec, Exclusives, Order,OnlineCalc, InstallmentPlan

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        
class ProductRecSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductRec
        fields = '__all__'
        
class ExclusivesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exclusives
        fields = '__all__'
        
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        
class OnlineCalcSerializer(serializers.ModelSerializer):
    class Meta:
        model = OnlineCalc
        fields = '__all__'
        
class InstallmentPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstallmentPlan
        fields = '__all__'