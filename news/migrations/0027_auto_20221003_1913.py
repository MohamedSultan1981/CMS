# Generated by Django 3.1.6 on 2022-10-03 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0026_auto_20210504_1126'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'managed': True, 'ordering': ['my_order'], 'verbose_name': 'خبر', 'verbose_name_plural': 'الاخبار'},
        ),
        migrations.AlterField(
            model_name='news',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='تاريخ ادخال الخبر'),
        ),
        migrations.AlterField(
            model_name='news',
            name='my_order',
            field=models.PositiveIntegerField(default=0, verbose_name='ترتيب الأخبار'),
        ),
        migrations.AlterField(
            model_name='news',
            name='newstype',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='news.newstype', verbose_name='نوع الخبر'),
        ),
        migrations.AlterField(
            model_name='news',
            name='newsurl',
            field=models.URLField(blank=True, max_length=1500, null=True, verbose_name='رابط الخبر'),
        ),
        migrations.AlterField(
            model_name='news',
            name='newsvideo',
            field=models.FileField(blank=True, null=True, upload_to='video/', verbose_name='رابط وسائط متعددة عن الخبر'),
        ),
        migrations.AlterField(
            model_name='news',
            name='slug',
            field=models.SlugField(allow_unicode=True, max_length=1500, verbose_name='العنوان الذي يظهرفي الرابط'),
        ),
        migrations.AlterField(
            model_name='news',
            name='status',
            field=models.CharField(choices=[('DF', 'Draft'), ('PB', 'Published'), ('WD', 'Withdraw')], default='DF', max_length=2, verbose_name='حالة الخبر'),
        ),
        migrations.AlterField(
            model_name='newsfile',
            name='newsid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='News_file', to='news.news'),
        ),
        migrations.AlterField(
            model_name='newsimages',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='photo/', verbose_name='الصورة'),
        ),
    ]