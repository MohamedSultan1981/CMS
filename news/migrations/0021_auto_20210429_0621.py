# Generated by Django 3.1.6 on 2021-04-29 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0020_auto_20210429_0447'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['my_order'], 'verbose_name': 'خبر', 'verbose_name_plural': 'الاخبار'},
        ),
        migrations.AlterModelOptions(
            name='newsfile',
            options={'verbose_name': 'ملف', 'verbose_name_plural': 'الملفات'},
        ),
        migrations.AlterModelOptions(
            name='newstype',
            options={'verbose_name': 'نوع الخبر', 'verbose_name_plural': 'انواع الاخبار'},
        ),
        migrations.AlterModelOptions(
            name='papertype',
            options={'verbose_name': 'جريدة', 'verbose_name_plural': 'الجرائد'},
        ),
        migrations.AlterField(
            model_name='news',
            name='negative',
            field=models.BooleanField(verbose_name='سلبي'),
        ),
        migrations.AlterField(
            model_name='news',
            name='newsvideo',
            field=models.URLField(blank=True, null=True, verbose_name='رابط وسائط متعددة عن الخبر'),
        ),
        migrations.RemoveField(
            model_name='news',
            name='papertype',
        ),
        migrations.AddField(
            model_name='news',
            name='papertype',
            field=models.ManyToManyField(null=True, to='news.PaperType', verbose_name='الجريدة'),
        ),
        migrations.AlterField(
            model_name='newsfile',
            name='filename',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='الملف'),
        ),
    ]
