# Generated by Django 5.1.2 on 2024-10-19 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_alter_book_author_alter_book_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.DecimalField(decimal_places=2, default=15, max_digits=10, verbose_name='Цена'),
            preserve_default=False,
        ),
    ]
