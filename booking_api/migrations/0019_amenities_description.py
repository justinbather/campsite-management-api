# Generated by Django 4.2.3 on 2023-08-25 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_api', '0018_amenities_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='amenities',
            name='description',
            field=models.TextField(default='No description available'),
        ),
    ]
