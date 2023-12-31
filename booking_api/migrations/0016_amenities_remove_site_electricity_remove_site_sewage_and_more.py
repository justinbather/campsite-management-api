# Generated by Django 4.2.3 on 2023-08-22 01:25

import booking_api.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_api', '0015_alter_siteimage_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Amenities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
            ],
        ),
        migrations.RemoveField(
            model_name='site',
            name='electricity',
        ),
        migrations.RemoveField(
            model_name='site',
            name='sewage',
        ),
        migrations.RemoveField(
            model_name='site',
            name='water',
        ),
        migrations.AlterField(
            model_name='site',
            name='thumbnail',
            field=models.ImageField(upload_to='./assets/thumbnails', validators=[booking_api.validators.image_validator]),
        ),
        migrations.AddField(
            model_name='site',
            name='amenities',
            field=models.ManyToManyField(related_name='Site', to='booking_api.amenities'),
        ),
    ]
