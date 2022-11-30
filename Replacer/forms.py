from django import forms
from .models import ReplaceField, Template, Customer
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
    # customer = forms.ModelMultipleChoiceField(label='Заказчик', queryset=Customer.objects.all(), widget=forms.Select(attrs = {"class":"form-control"}), empty_label=None)
    # customer = forms.ModelChoiceField(label='Заказчик', queryset=Customer.objects.all(), widget=forms.Select(attrs = {"class":"form-control"}), empty_label='empty', required=False)
    customer = forms.ModelChoiceField(label='Заказчик', queryset=Customer.objects.all(), widget=forms.Select(attrs = {"class":"form-control"}), empty_label=None)
    
    
