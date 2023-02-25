# Generated by Django 4.1.1 on 2022-12-05 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Replacer', '0011_company_alter_customer_options_alter_customer_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, db_index=True, max_length=255, verbose_name='Подпись')),
                ('sign_title', models.TextField(blank=True, max_length=255, verbose_name='Должность')),
                ('sign', models.CharField(blank=True, db_index=True, max_length=255, verbose_name='Инициал Фамилия')),
            ],
        ),
        migrations.AlterField(
            model_name='company',
            name='company_abb',
            field=models.CharField(blank=True, db_index=True, max_length=255, verbose_name='Компания сокращенно'),
        ),
        migrations.AlterField(
            model_name='company',
            name='company_address',
            field=models.TextField(blank=True, max_length=255, verbose_name='Адресc'),
        ),
    ]