from django.urls import path
from apps.products.views import ProductAPIView, ProductCreateAPIView, ProductRecCreateAPIView, ExclusivesCreateAPIView, OrderCreateAPIView, OnlineCalcCreateAPIView, InstallmentPlanCreateAPIView

urlpatterns = [
    path('', ProductAPIView.as_view()),
    path('create/', ProductCreateAPIView.as_view()),
    path('product_rec/', ProductRecCreateAPIView.as_view()),
    path('exclusives/', ExclusivesCreateAPIView.as_view()),
    path('order/', OrderCreateAPIView.as_view()),
    path('online_calc/', OnlineCalcCreateAPIView.as_view()),
    path('installment/', InstallmentPlanCreateAPIView.as_view()),
]