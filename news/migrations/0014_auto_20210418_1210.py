# Generated by Django 3.1.5 on 2021-04-18 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0013_auto_20210404_1356'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['my_order']},
        ),
        migrations.AddField(
            model_name='news',
            name='my_order',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
