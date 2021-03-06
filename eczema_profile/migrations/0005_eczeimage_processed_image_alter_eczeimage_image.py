# Generated by Django 4.0.1 on 2022-01-31 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eczema_profile', '0004_remove_eczeimage_profile_eczeimage_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='eczeimage',
            name='processed_image',
            field=models.ImageField(null=True, upload_to='ProcessedEczeImage'),
        ),
        migrations.AlterField(
            model_name='eczeimage',
            name='image',
            field=models.ImageField(null=True, upload_to='EczeImages'),
        ),
    ]
