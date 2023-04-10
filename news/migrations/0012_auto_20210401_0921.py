# Generated by Django 3.1.5 on 2021-04-01 07:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0011_auto_20210401_0914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='newstype',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='news.newstype', verbose_name='نوع الخبر'),
        ),
        migrations.AlterField(
            model_name='news',
            name='papertype',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='news.papertype', verbose_name='الجريدة'),
        ),
    ]