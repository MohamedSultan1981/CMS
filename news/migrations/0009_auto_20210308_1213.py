# Generated by Django 3.1.5 on 2021-03-08 10:13

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_news_newsembedvideo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='newsscript',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='newstype',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='news.newstype'),
        ),
        migrations.AlterField(
            model_name='news',
            name='papertype',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='news.papertype'),
        ),
    ]
