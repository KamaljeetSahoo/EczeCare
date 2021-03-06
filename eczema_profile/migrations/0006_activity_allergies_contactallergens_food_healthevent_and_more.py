# Generated by Django 4.0.1 on 2022-02-01 14:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('eczema_profile', '0005_eczeimage_processed_image_alter_eczeimage_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Allergies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allergy_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ContactAllergens',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_allergy_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='HealthEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('health_event_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Trigger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eczema_profile.activity')),
                ('allergy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eczema_profile.allergies')),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eczema_profile.contactallergens')),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eczema_profile.food')),
                ('health_event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eczema_profile.healthevent')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eczema_profile.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
