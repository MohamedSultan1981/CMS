# Generated by Django 3.1.6 on 2022-10-18 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0030_auto_20221018_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='slug',
            field=models.SlugField(allow_unicode=True, blank=True, max_length=1500, null=True, verbose_name='العنوان الذي يظهرفي الرابط'),
        ),
    ]