# Generated by Django 4.1.1 on 2022-11-28 11:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Replacer', '0005_remove_replacefield_owner_alter_template_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='replacefield',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Владелец'),
        ),
    ]
