# Generated by Django 3.0.8 on 2020-09-15 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20200914_1820'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='Women',
        ),
        migrations.RemoveField(
            model_name='product',
            name='mens',
        ),
        migrations.AddField(
            model_name='product',
            name='men',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='women',
            field=models.BooleanField(default=False),
        ),
    ]
