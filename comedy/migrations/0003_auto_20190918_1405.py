# Generated by Django 2.2.5 on 2019-09-18 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comedy', '0002_auto_20190311_1655'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='name',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='article',
            name='title',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
