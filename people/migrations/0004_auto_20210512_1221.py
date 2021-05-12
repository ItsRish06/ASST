# Generated by Django 3.1.7 on 2021-05-12 06:51

from django.db import migrations, models
import people.models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0003_people_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='image',
            field=models.ImageField(blank=True, default='avatar.png', null=True, upload_to=people.models.upload_location),
        ),
    ]