# Generated by Django 4.2.11 on 2024-04-05 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipients', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipient',
            name='city',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='recipient',
            name='country',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='recipient',
            name='first_name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='recipient',
            name='last_name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='recipient',
            name='mobile_number',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]
