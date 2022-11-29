from pyexpat import model
from django import forms
from django.contrib import admin
from .models import Template, ReplaceField, Customer
from django.utils.safestring import mark_safe


class TemplateAdmin(admin.ModelAdmin):
    field = '__all__'


class ReplaceFieldAdmin(admin.ModelAdmin):
    field = '__all__'


class CustomerAdmin(admin.ModelAdmin):
    field = '__all__'


admin.site.register(Template, TemplateAdmin)
admin.site.register(ReplaceField, ReplaceFieldAdmin)
admin.site.register(Customer, CustomerAdmin)
