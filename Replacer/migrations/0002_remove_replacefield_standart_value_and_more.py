# Generated by Django 4.1.1 on 2022-11-18 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Replacer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='replacefield',
            name='standart_value',
        ),
        migrations.AlterField(
            model_name='replacefield',
            name='replace_value',
            field=models.TextField(verbose_name='Значение'),
        ),
    ]
