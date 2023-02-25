from pyexpat import model
from django import forms
from django.contrib import admin
from .models import Template, ReplaceField, Customer, Company, Sign
from django.utils.safestring import mark_safe


class TemplateAdmin(admin.ModelAdmin):
    field = '__all__'


class ReplaceFieldAdmin(admin.ModelAdmin):
    field = '__all__'


class CustomerAdmin(admin.ModelAdmin):
    field = '__all__'
    list_display = ('title','customer','customer_abb',)
    search_fields = ('title',)


class CompanyAdmin(admin.ModelAdmin):
    field = '__all__'
    list_display = ('company_abb','company_title','manager_name','company_address','manager_full_name',)
    #list_editable = ('company_title','manager_name','company_address','manager_full_name',)
    search_fields = ('company_abb',)

class SignAdmin(admin.ModelAdmin):
    field = '__all__'
    list_display = ('title','sign',)
    

admin.site.register(Template, TemplateAdmin)
admin.site.register(ReplaceField, ReplaceFieldAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Sign, SignAdmin)
