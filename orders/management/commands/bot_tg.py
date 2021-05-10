import time
import requests


from orders.models import Order
from django.conf import settings
from django.core.management import BaseCommand

# {order.id_ordered}
class Command(BaseCommand):
    help = 'telegram-bot'

    def handle(self, *args, **options):

        bot_api_key = settings.TOKEN
        print(bot_api_key)
        chanale_name = '@Sonunfashion1'
        print(chanale_name)
        order = Order.objects.all()
        message = f'''
            Здравствуйте, Вас приветствует бот Sonufashion!!!
            Заказ № {Order.id}
            Имя:  {Order.first_name}
            Фамилия:  {Order.last_name}
            Номер:  {Order.phone}
            Адрес:  {Order.address}
            --------------------------
            Что заказали:
            {Order.products}
            --------------------------
        '''
        params = {
            'chat_id' : chanale_name,
            'text' : message,
        }
        # url = f'http://api.telegram.org/bot{bot_api_key}/sendMessage'


        # print(url)
        # print(requests.get(url, params = params).content)


        print(order)

        for orders in order:
            print(order)