# Generated by Django 5.1.3 on 2024-12-14 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Car_App', '0002_alter_car_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]