from django.db import models


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


class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name='Категории')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Size(models.Model):
    size = models.CharField(max_length=255, verbose_name="Размер")
    count = models.IntegerField(verbose_name="Количество в пачке")

    class Meta:
        # ordering = "name"
        verbose_name = "Размер"
        verbose_name_plural = "Размеры"

    def __str__(self):
        return self.size


class Product(models.Model):
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    title = models.CharField(max_length=50, verbose_name='Наименование', db_index=True)
    slug = models.SlugField(unique=True, db_index=True, max_length=200)
    image = models.ImageField(upload_to='media', null=True, blank=True, verbose_name='Изображение')
    image2 = models.ImageField(upload_to='media', null=True, blank=True, verbose_name='Изображение')
    image3 = models.ImageField(upload_to='media', null=True, blank=True, verbose_name='Изображение')
    image4 = models.ImageField(upload_to='media', null=True, blank=True, verbose_name='Изображение')
    image5 = models.ImageField(upload_to='media', null=True, blank=True, verbose_name='Изображение')
    image6 = models.ImageField(upload_to='media', null=True, blank=True, verbose_name='Изображение')
    image7 = models.ImageField(upload_to='media', null=True, blank=True, verbose_name='Изображение')
    image8 = models.ImageField(upload_to='media', null=True, blank=True, verbose_name='Изображение')
    image9 = models.ImageField(upload_to='media', null=True, blank=True, verbose_name='Изображение')
    image10 = models.ImageField(upload_to='media', null=True, blank=True, verbose_name='Изображение')
    discription = models.TextField(verbose_name='Описание', null=True)
    size = models.ForeignKey(Size, verbose_name='Размер', blank=True, null=True, on_delete=models.CASCADE)
    color = models.CharField(max_length=200, verbose_name='цвет', null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')
    available = models.BooleanField(default=True, verbose_name='Наличие товара')

    class Meta:
        ordering = ('title',)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.title
