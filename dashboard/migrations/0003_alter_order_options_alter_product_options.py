# Generated by Django 4.1.4 on 2022-12-24 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name_plural': 'Staff'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name_plural': 'Product'},
        ),
    ]
