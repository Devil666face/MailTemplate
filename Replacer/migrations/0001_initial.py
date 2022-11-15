# Generated by Django 4.1.1 on 2022-11-14 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=255, verbose_name='Наименование шаблона')),
                ('file', models.FileField(upload_to='templates/%Y/%m/%d/', verbose_name='Файл шаблона')),
            ],
            options={
                'verbose_name': 'Шаблон',
                'verbose_name_plural': 'Шаблоны',
                'ordering': ['pk'],
            },
        ),
        migrations.CreateModel(
            name='ReplaceField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=255, verbose_name='Имя поля для замены')),
                ('standart_value', models.TextField(verbose_name='Значение по умолчанию')),
                ('replace_value', models.TextField(verbose_name='Значение для замены')),
                ('tag', models.CharField(max_length=255, verbose_name='Тэг')),
                ('template', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Replacer.template', verbose_name='Id шаблона')),
            ],
            options={
                'verbose_name': 'Заменяемое поле',
                'verbose_name_plural': 'Заменяемые поля',
                'ordering': ['template'],
            },
        ),
    ]
