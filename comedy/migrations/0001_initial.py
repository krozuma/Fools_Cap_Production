# Generated by Django 2.2.5 on 2019-09-10 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateField()),
                ('headline', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('pic', models.ImageField(blank=True, upload_to='images')),
                ('rank', models.IntegerField(default=0)),
                ('cite', models.CharField(blank=True, max_length=200)),
                ('art_cat', models.CharField(choices=[('NE', 'News'), ('PO', 'Politics'), ('SP', 'Sports'), ('LO', 'Local'), ('OP', 'Opinion'), ('HE', 'Health'), ('EN', 'Entertainment')], default='NE', max_length=2)),
            ],
        ),
    ]
