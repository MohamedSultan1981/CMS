# Generated by Django 3.1.5 on 2021-01-19 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20210119_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsfile',
            name='newsid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='News', to='news.news'),
        ),
    ]
