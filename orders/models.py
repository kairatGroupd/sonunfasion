from django.db import models
from sonun.models import Product


class Order(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Имя заказчика')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия заказчика')
    phone = models.CharField(max_length=200, verbose_name='Номер телефона', blank=True, null=True)
    email = models.EmailField()
    address = models.CharField(max_length=250, verbose_name='Адрес')
    postal_code = models.CharField(max_length=20, verbose_name='Код')
    city = models.CharField(max_length=100, verbose_name='Город')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата обнавления', blank=True, null=True)
    products = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Order {}'.format(self.id)


