# Generated by Django 4.0.2 on 2022-04-24 06:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apicalls', '0010_blogsection_mediades'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogsection',
            options={'ordering': ['pk', 'timestamp']},
        ),
        migrations.AddField(
            model_name='blogsection',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 24, 11, 39, 56, 527654)),
        ),
    ]