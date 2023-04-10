# Generated by Django 3.1.5 on 2021-04-01 07:14

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0010_auto_20210401_0908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='negative',
            field=models.BooleanField(verbose_name='أخبار سلبية'),
        ),
        migrations.AlterField(
            model_name='news',
            name='newsdate',
            field=models.DateField(verbose_name='تاريخ نشر الخبر'),
        ),
        migrations.AlterField(
            model_name='news',
            name='newsscript',
            field=tinymce.models.HTMLField(blank=True, null=True, verbose_name='تفاصيل الخبر'),
        ),
        migrations.AlterField(
            model_name='news',
            name='newsurl',
            field=models.URLField(blank=True, null=True, verbose_name='رابط الخبر'),
        ),
        migrations.AlterField(
            model_name='newstype',
            name='newsName',
            field=models.CharField(max_length=200, verbose_name='نوع الخبر'),
        ),
        migrations.AlterField(
            model_name='papertype',
            name='paperName',
            field=models.CharField(max_length=200, verbose_name='الجريدة'),
        ),
    ]
