# Generated by Django 4.0.2 on 2022-04-05 17:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apicalls', '0002_alter_mediacontent_mediadate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mediacontent',
            name='mediaDate',
            field=models.DateField(default=datetime.date(2022, 4, 5)),
        ),
        migrations.AlterField(
            model_name='mediacontent',
            name='mediaDescription',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='project',
            name='projectDate',
            field=models.DateField(default=datetime.date(2022, 4, 5)),
        ),
        migrations.AlterField(
            model_name='project',
            name='projectDescription',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='section',
            name='sectionDate',
            field=models.DateField(default=datetime.date(2022, 4, 5)),
        ),
        migrations.AlterField(
            model_name='section',
            name='sectionDescription',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='section',
            name='sectionDisplayType',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]