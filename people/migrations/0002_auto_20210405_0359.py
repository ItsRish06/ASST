# Generated by Django 3.1.7 on 2021-04-04 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitor',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='time',
            field=models.TimeField(auto_now_add=True),
        ),
    ]
