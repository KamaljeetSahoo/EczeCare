# Generated by Django 3.2.5 on 2022-02-02 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eczema_profile', '0007_remove_trigger_activity_trigger_activity_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='poemscore',
            name='hum',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='poemscore',
            name='temp',
            field=models.DecimalField(decimal_places=2, default=20.0, max_digits=5),
            preserve_default=False,
        ),
    ]
