# Generated by Django 2.2 on 2020-08-22 19:12

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('k12_app', '0002_auto_20200822_1659'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='upvote',
        ),
        migrations.AddField(
            model_name='answer',
            name='upvote',
            field=models.ManyToManyField(blank=True, null=True, related_name='upvote', to=settings.AUTH_USER_MODEL),
        ),
    ]
