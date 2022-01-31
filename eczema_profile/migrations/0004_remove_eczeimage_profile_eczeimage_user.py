# Generated by Django 4.0.1 on 2022-01-31 18:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('eczema_profile', '0003_alter_poemscore_q1_alter_poemscore_q2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eczeimage',
            name='profile',
        ),
        migrations.AddField(
            model_name='eczeimage',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
