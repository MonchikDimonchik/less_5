# Generated by Django 5.1.2 on 2024-10-20 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_book_storage_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='in_stock',
        ),
    ]
