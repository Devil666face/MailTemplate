from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# class CustomUser(AbstractUser):
#     phone = models.CharField(max_length=255, blank=True,verbose_name='Номер телефона')


class Template(models.Model):
    title = models.CharField(max_length=255, db_index=True, verbose_name='Наименование шаблона')
    file = models.FileField(upload_to='templates/%Y/%m/%d/', blank=False, verbose_name='Файл шаблона')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Владелец')

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse('template', kwargs={"pk": self.pk})

    class Meta:
        verbose_name = 'Шаблон'
        verbose_name_plural = 'Шаблоны'
        ordering = ['pk']


class ReplaceField(models.Model):
    title = models.CharField(
        max_length=255, db_index=True, verbose_name='Имя поля для замены')
    replace_value = models.TextField(blank=True, verbose_name='Значение')
    tag = models.CharField(max_length=255, verbose_name='Тэг')
    template = models.ForeignKey(
        Template, on_delete=models.CASCADE, null=False, verbose_name='Id шаблона')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Владелец')

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Заменяемое поле'
        verbose_name_plural = 'Заменяемые поля'
        ordering = ['template']


class Customer(models.Model):
    title = models.CharField(max_length=255, blank=True, db_index=True, verbose_name='Заказчик')
    customer = models.TextField(blank=True, verbose_name='Текст заказчика для замены')
    customer_abb = models.CharField(max_length=255, blank=True, verbose_name='Сокращение ОВУ')

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Заказчик'
        verbose_name_plural = 'Заказчики'
        ordering = ['-pk']
