# Generated by Django 3.1.6 on 2021-04-29 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0021_auto_20210429_0621'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='status',
            field=models.CharField(choices=[('d', 'Draft'), ('p', 'Published'), ('w', 'Withdrawn')], default='d', max_length=1),
        ),
    ]
