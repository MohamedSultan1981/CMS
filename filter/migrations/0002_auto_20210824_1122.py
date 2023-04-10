# Generated by Django 3.1.6 on 2021-08-24 09:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filter', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='facility_data',
            options={'managed': False, 'ordering': ['FACILITY_ID']},
        ),
        migrations.AlterModelOptions(
            name='facility_products',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='industrial_products',
            options={'managed': False, 'ordering': ['PRODUCT_TITLE']},
        ),
        migrations.AlterModelOptions(
            name='industrial_registry',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='measuring_units',
            options={'managed': False},
        ),
    ]