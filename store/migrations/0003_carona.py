# Generated by Django 3.2.2 on 2021-05-17 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20210516_1252'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carona',
            fields=[
                ('jid', models.AutoField(primary_key=True, serialize=False)),
                ('jname', models.CharField(max_length=55)),
                ('jyear', models.IntegerField(max_length=5)),
            ],
        ),
    ]
