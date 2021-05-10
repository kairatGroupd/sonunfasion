# APIview

from rest_framework.generics import ListCreateAPIView
from django_filters.rest_framework import DjangoFilterBackend
from sonun.models import *
from orders.models import *
from api.serializers import CategorySerializer, ProductSerializer, StockSerializer, OrderSerializer, SizeSerializer
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.views import APIView

# The telegram bot exempl

from django.views.decorators.http import require_http_methods
import time
import datetime
import requests
from django.conf import settings


class SizeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Size.objects.all()
    serializer_class = SizeSerializer
    # filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    # filter_fields = 'size'

class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ['category',]

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class StockViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer


# Bot configuretion




class OrderViewset(viewsets.ReadOnlyModelViewSet, ListCreateAPIView):
	queryset = Order.objects.all()
	serializer_class = OrderSerializer



# order_now = Order.objects.all().order_by('-id')[:1].id
# print(order_now)

# order_now = Order.objects.all().last().id
# print(order_now)


# bot_api_key = settings.TOKEN  
# print(bot_api_key)
# chanale_name = '@Sonunfashion1'
# message = f'''
#     Здравствуйте, Вас приветствует бот Sonufashion!!!
#     Заказ № {OrderViewset.queryset.latest}
#     --------------------------
# '''
# params = {
#     'chat_id' : chanale_name,
#     'text' : message,
# }

# if Order.objects.all().list('created') >= datetime.date.today(strptime(string, '%Y-%m-%dT%H:%M:%S.%fZ')):
    
#     url = f'http://api.telegram.org/bot{bot_api_key}/sendMessage'
#     print(url)
#     print(requests.get(url, params = params).content)
# else:
#     print("Я проверил сайт, пока нет заказов")



    
