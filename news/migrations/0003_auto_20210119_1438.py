# Generated by Django 3.1.5 on 2021-01-19 12:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_newsfiles'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='NewsFiles',
            new_name='NewsFile',
        ),
    ]