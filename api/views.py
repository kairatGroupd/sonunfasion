from rest_framework.generics import ListCreateAPIView
from sonun.models import *
from orders.models import *
from api.serializers import CategorySerializer, ProductSerializer, StockSerializer, OrderSerializer, SizeSerializer
from rest_framework import viewsets


class SizeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Size.objects.all()
    serializer_class = SizeSerializer

class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class StockViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

class OrderViewset(viewsets.ReadOnlyModelViewSet, ListCreateAPIView):
	queryset = Order.objects.all()
	serializer_class = OrderSerializer
