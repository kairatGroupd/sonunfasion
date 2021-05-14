# APIview
from urllib import response

from rest_framework.generics import ListCreateAPIView
from django_filters.rest_framework import DjangoFilterBackend
from sonun.models import *
from orders.models import *
from api.serializers import CategorySerializer, ProductSerializer, StockSerializer, OrderSerializer, SizeSerializer
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

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


bot_api_key = settings.TOKEN  
print(bot_api_key)
chanale_name = '@Sonunfashion1'



def tgapi(order_tg):
    messages = f'''
    Здравствуйте, Вас приветствует бот Sonufashion!!!
    Заказ №: {order_tg.id}
    Имя заказчика: {order_tg.first_name}
    Фамилия заказчика: {order_tg.last_name}
    Номер телефона: {order_tg.phone}
    Почта Email: {order_tg.email}
    Адрес: {order_tg.address}
    Почтовый индекс: {order_tg.postal_code}
    Город: {order_tg.city}
    Дата создания: {order_tg.created}
    --------------------------
    Что заказали:
    {order_tg.products}
    '''
    params = {
        'chat_id' : chanale_name,
        'text' : messages,
    }
    url = f'http://api.telegram.org/bot{bot_api_key}/sendMessage'
    requests.get(url, params = params).content


class OrderView(APIView):

    def get(self, request, *args, **kwargs):
        questions = Order.objects.all()
        serializer = OrderSerializer(questions, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = OrderSerializer(data=request.data)

        
        # order_tg = 'hell'
        if serializer.is_valid():
            question = serializer.save()
            tgapi(question)
            serializer = OrderSerializer(question)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





    
