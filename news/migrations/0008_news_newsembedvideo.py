# Generated by Django 3.1.5 on 2021-03-01 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_auto_20210301_0850'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='newsembedvideo',
            field=models.TextField(blank=True, null=True),
        ),
    ]
