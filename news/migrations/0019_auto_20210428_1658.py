# Generated by Django 3.1.6 on 2021-04-28 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0018_auto_20210428_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='slug',
            field=models.SlugField(allow_unicode=True, null=True, unique=True),
        ),
    ]
