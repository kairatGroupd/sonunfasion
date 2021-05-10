from django.db import models

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# Create your models here.
class Stock(models.Model):
    name = models.CharField(max_length=300, verbose_name='Название акции', blank=True, null=True)
    image = models.ImageField(upload_to='media', null=True, blank=True, verbose_name='Изображение 1200х300')
    available = models.BooleanField(default=True, verbose_name='Актуальность акции')

    class Meta:
        verbose_name = 'Акция'
        verbose_name_plural = 'Акции'

    def __str__(self):
        return self.name

class Color(models.Model):
    color = models.CharField(max_length = 300, verbose_name= "Цвет")

    class Meta:
        ordering = ['color']
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'

    def __str__(self):
        return self.color

class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name='Категории')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Size(models.Model):
    size = models.CharField(max_length=255, verbose_name="Размер", blank=True)
    # count = models.IntegerField(verbose_name="Количество в пачке")

    class Meta:
        ordering = ['size']
        verbose_name = "Размер"
        verbose_name_plural = "Размеры"

    def __str__(self):
        return self.size


class Product(models.Model):
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.DO_NOTHING,null= True, related_name='category' )
    title = models.CharField(max_length=50, verbose_name='Наименование', db_index=True)
    slug = models.SlugField(unique=True, db_index=True, max_length=200)
    image = models.ImageField(upload_to='media', null=True, blank=True, verbose_name='Изображение')
    image_thumbnail  =  ImageSpecField ( source = 'image' ,
                                       processors = [ ResizeToFill ( 1920 , 1080 )],
                                       format = 'JPEG' ,
                                       options = { 'quality': 60 })
    image2 = models.ImageField(upload_to='media', null=True, blank=True, verbose_name='Изображение')
    image2_thumbnail  =  ImageSpecField ( source = 'image2' ,
                                       processors = [ ResizeToFill ( 1920 , 1080 )],
                                       format = 'JPEG' ,
                                       options = { 'quality': 60 })
    image3 = models.ImageField(upload_to='media', null=True, blank=True, verbose_name='Изображение')
    image3_thumbnail  =  ImageSpecField ( source = 'image3' ,
                                       processors = [ ResizeToFill ( 1920 , 1080 )],
                                       format = 'JPEG' ,
                                       options = { 'quality': 60 })
    image4 = models.ImageField(upload_to='media', null=True, blank=True, verbose_name='Изображение')
    image4_thumbnail  =  ImageSpecField ( source = 'image4' ,
                                       processors = [ ResizeToFill ( 1920 , 1080 )],
                                       format = 'JPEG' ,
                                       options = { 'quality': 60 })
    image5 = models.ImageField(upload_to='media', null=True, blank=True, verbose_name='Изображение')
    image5_thumbnail  =  ImageSpecField ( source = 'image5' ,
                                       processors = [ ResizeToFill ( 1920 , 1080 )],
                                       format = 'JPEG' ,
                                       options = { 'quality': 60 })
    image6 = models.ImageField(upload_to='media', null=True, blank=True, verbose_name='Изображение')
    image6_thumbnail  =  ImageSpecField ( source = 'image6' ,
                                       processors = [ ResizeToFill ( 1920 , 1080 )],
                                       format = 'JPEG' ,
                                       options = { 'quality': 60 })
    image7 = models.ImageField(upload_to='media', null=True, blank=True, verbose_name='Изображение')
    image8 = models.ImageField(upload_to='media', null=True, blank=True, verbose_name='Изображение')
    image9 = models.ImageField(upload_to='media', null=True, blank=True, verbose_name='Изображение')
    image10 = models.ImageField(upload_to='media', null=True, blank=True, verbose_name='Изображение')

    discription = models.TextField(verbose_name='Описание', null=True)
    size = models.ManyToManyField(Size, verbose_name='Размер', blank=True, related_name="size_c")
    color = models.ManyToManyField(Color, verbose_name='цвет',blank=True,)
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')
    count = models.IntegerField(verbose_name = 'Сколько шт в одном размере', null=True, blank=True)
    available = models.BooleanField(default=True, verbose_name='Наличие товара')

    class Meta:
        ordering = ('title',)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.title
