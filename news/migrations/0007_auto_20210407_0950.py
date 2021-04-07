# Generated by Django 3.1.8 on 2021-04-07 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_auto_20210407_0949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='country_of_news',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='news',
            name='news_url',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='news',
            name='source_of_news',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
