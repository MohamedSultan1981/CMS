# Generated by Django 3.1.5 on 2021-04-01 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_auto_20210308_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=1500, verbose_name='العنوان'),
        ),
    ]
