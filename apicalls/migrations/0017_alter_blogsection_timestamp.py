# Generated by Django 4.0.2 on 2022-05-09 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apicalls', '0016_alter_blogsection_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogsection',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
