# Generated by Django 4.1.5 on 2023-01-31 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_road_length'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint',
            name='cityname',
            field=models.CharField(default=0, max_length=255),
        ),
    ]
