# Generated by Django 5.1.2 on 2024-10-14 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=100)),
                ('published_date', models.DateField()),
                ('isbn_number', models.CharField(max_length=13)),
                ('pages', models.IntegerField()),
                ('language', models.CharField(max_length=10)),
                ('description', models.TextField()),
            ],
        ),
    ]