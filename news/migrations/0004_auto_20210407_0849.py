# Generated by Django 3.1.8 on 2021-04-07 08:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_news_news_url'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'News', 'verbose_name_plural': 'News'},
        ),
        migrations.AlterModelTable(
            name='news',
            table='news',
        ),
    ]
