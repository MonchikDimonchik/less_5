# Generated by Django 5.1.2 on 2024-10-19 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_book_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='in_stock',
            field=models.BooleanField(default=True, verbose_name='В наличии'),
        ),
    ]