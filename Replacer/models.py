from django.db import models
from django.urls import reverse


class Template(models.Model):
    title = models.CharField(max_length=255, db_index=True, verbose_name='Наименование шаблона')
    file = models.FileField(upload_to='templates/%Y/%m/%d/',blank=False, verbose_name='Файл шаблона')

    def __str__(self) -> str:
            return self.title

    def get_absolute_url(self):
        return reverse('template', kwargs={"pk":self.pk})

    class Meta:
        verbose_name = 'Шаблон'
        verbose_name_plural= 'Шаблоны'
        ordering = ['pk']


class ReplaceField(models.Model):
    title = models.CharField(max_length=255, db_index=True, verbose_name='Имя поля для замены')
    standart_value = models.TextField(blank=False, verbose_name='Значение по умолчанию')
    replace_value = models.TextField(blank=False, verbose_name='Значение для замены')
    tag = models.CharField(max_length=255, verbose_name='Тэг')
    template = models.ForeignKey(Template, on_delete=models.PROTECT, null=False, verbose_name='Id шаблона')

    def __str__(self) -> str:
         return self.title

    class Meta:
        verbose_name = 'Заменяемое поле'
        verbose_name_plural = 'Заменяемые поля'
        ordering = ['template']