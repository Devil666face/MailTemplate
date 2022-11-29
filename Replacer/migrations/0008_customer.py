# Generated by Django 4.1.1 on 2022-11-29 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Replacer', '0007_alter_replacefield_replace_value'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=255, verbose_name='Заказчик')),
                ('customer', models.TextField(verbose_name='Текст заказчика для замены')),
                ('customer_add', models.CharField(db_index=True, max_length=255, verbose_name='Сокращение ОВУ')),
            ],
            options={
                'verbose_name': 'Заказчик',
                'verbose_name_plural': 'Заказчики',
                'ordering': ['pk'],
            },
        ),
    ]
