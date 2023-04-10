# Generated by Django 3.1.6 on 2021-04-30 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0022_news_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='newsurl',
            field=models.URLField(blank=True, default='--', max_length=1500, null=True, verbose_name='رابط الخبر'),
        ),
        migrations.AlterField(
            model_name='news',
            name='status',
            field=models.CharField(choices=[('d', 'قيد النشر و التعديل'), ('p', 'نشر'), ('w', 'سحب')], default='d', max_length=1, verbose_name='حالة الخبر'),
        ),
    ]
