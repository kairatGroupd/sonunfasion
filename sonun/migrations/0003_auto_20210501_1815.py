# Generated by Django 3.0 on 2021-05-01 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sonun', '0002_auto_20210501_1801'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='size',
            options={'ordering': ['size'], 'verbose_name': 'Размер', 'verbose_name_plural': 'Размеры'},
        ),
        migrations.RemoveField(
            model_name='size',
            name='count',
        ),
        migrations.AlterField(
            model_name='size',
            name='size',
            field=models.CharField(max_length=255, null=True, verbose_name='Размер'),
        ),
    ]