# Generated by Django 2.1.7 on 2019-03-11 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comedy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='pic',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]
