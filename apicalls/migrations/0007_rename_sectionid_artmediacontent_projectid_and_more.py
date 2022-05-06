# Generated by Django 4.0.2 on 2022-04-19 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apicalls', '0006_artproject_artmediacontent'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artmediacontent',
            old_name='sectionID',
            new_name='projectID',
        ),
        migrations.AlterField(
            model_name='artmediacontent',
            name='videoUrl',
            field=models.TextField(blank=True, default=''),
        ),
    ]
