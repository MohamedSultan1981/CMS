# Generated by Django 3.1.6 on 2021-04-27 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0016_news_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
