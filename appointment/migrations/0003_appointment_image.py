# Generated by Django 3.2.2 on 2021-05-17 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0002_remove_appointment_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]