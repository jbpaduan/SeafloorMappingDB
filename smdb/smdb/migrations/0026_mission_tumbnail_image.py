# Generated by Django 3.2.7 on 2021-09-14 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smdb', '0025_mission_thumbnail_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='mission',
            name='tumbnail_image',
            field=models.ImageField(blank=True, upload_to='smdb/media'),
        ),
    ]
