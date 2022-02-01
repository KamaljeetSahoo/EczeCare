# Generated by Django 4.0.1 on 2022-02-01 21:23

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctorprofile',
            name='patients',
            field=models.ManyToManyField(related_name='patients', to=settings.AUTH_USER_MODEL),
        ),
    ]
