from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


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
    replace_value = models.TextField(blank=False, verbose_name='Значение')
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
