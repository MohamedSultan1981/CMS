# Generated by Django 3.1.6 on 2022-10-19 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0031_auto_20221018_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='slug',
            field=models.SlugField(allow_unicode=True, max_length=1500, unique_for_date='newsdate', verbose_name='العنوان الذي يظهرفي الرابط'),
        ),
    ]