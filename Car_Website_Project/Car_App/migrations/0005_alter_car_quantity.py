# Generated by Django 5.1.3 on 2024-12-16 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Car_App', '0004_remove_brand_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]
