from django import forms
from .models import ReplaceField, Template, Customer, Company, Sign
from django.contrib.auth.forms import AuthenticationForm

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Имя пользователя"}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={
        "class": "form-control",
        "placeholder": "Пароль"}))


class BootstrapForm(forms.ModelForm):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class TemplateBaseForm(BootstrapForm):
    class Meta:
        model = Template
        fields = ('title','file')


class FieldsBaseForm(BootstrapForm):
    class Meta:
        model = ReplaceField
        fields = ('title','replace_value','tag','template')
        widgets = {
            'template':forms.Select(attrs = {"class":"form-control", "style":"display: none;"},),    
        }
        labels = {
            'template': '',
        }


class ReplaceFieldFormUpdate(BootstrapForm):
    class Meta:
        model = ReplaceField
        fields = ['id', 'title', 'replace_value', 'tag']
        widgets = {
            'replace_value':forms.Textarea(attrs = {"rows":"4",},),
        }


class DocNameForm(forms.Form):
    doc_name = forms.CharField(label='Имя документа', max_length=100, widget=forms.TextInput(attrs = {"class":"form-control"}))


class CustomerForm(forms.Form):
    # customer = forms.ModelChoiceField(label='Заказчик', queryset=Customer.objects.all(), widget=forms.Select(attrs = {"class":"form-control"}), empty_label='empty', required=False)
    customer = forms.ModelChoiceField(label='Заказчик', queryset=Customer.objects.all(), widget=forms.Select(attrs = {"class":"form-control"}), empty_label=None)
    
    
class CompanyForm(forms.Form):
    company = forms.ModelChoiceField(label='Компания', queryset=Company.objects.all(), widget=forms.Select(attrs = {"class":"form-control"}), empty_label=None)


class ServiceForm(forms.Form):
    month = forms.CharField(label='Месяц', max_length=100, widget=forms.TextInput(attrs = {"class":"form-control"}))
    enter_date = forms.CharField(label='Входящая дата', max_length=100, widget=forms.TextInput(attrs = {"class":"form-control"})) 
    enter_num_org = forms.CharField(label='Входящий номер организации', required=False, max_length=100, widget=forms.TextInput(attrs = {"class":"form-control"}))
    date = forms.CharField(label='Дата печати письма', max_length=100, widget=forms.TextInput(attrs = {"class":"form-control"}))
    
class SignForm(forms.Form):
    sign = forms.ModelChoiceField(label='Подпись', queryset=Sign.objects.all(), widget=forms.Select(attrs = {"class":"form-control"}), empty_label=None)
