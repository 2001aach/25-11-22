# Generated by Django 4.1.3 on 2022-11-23 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpage',
            name='address',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='userpage',
            name='housenumber',
            field=models.IntegerField(max_length=15),
        ),
        migrations.AlterField(
            model_name='userpage',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
