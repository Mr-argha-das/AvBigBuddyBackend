# Generated by Django 4.2.6 on 2023-10-09 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wallpaper', '0002_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tags',
            name='name',
        ),
    ]
