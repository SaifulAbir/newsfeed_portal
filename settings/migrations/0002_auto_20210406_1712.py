# Generated by Django 3.1.8 on 2021-04-06 17:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='modified_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='country',
            name='modified_by',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='country',
            name='modified_from',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='keyword',
            name='modified_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='keyword',
            name='modified_by',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='keyword',
            name='modified_from',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='settings',
            name='modified_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='settings',
            name='modified_by',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='settings',
            name='modified_from',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='settings',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, related_name='settings', to='auth.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='source',
            name='modified_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='source',
            name='modified_by',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='source',
            name='modified_from',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
