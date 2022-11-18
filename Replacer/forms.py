from django import forms
from .models import ReplaceField, Template


class BootstrapForm(forms.ModelForm):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class TemplateBaseForm(BootstrapForm):
    class Meta:
        model = Template
        fields = '__all__'


class ReplaceFieldFormUpdate(BootstrapForm):
    class Meta:
        model = ReplaceField
        fields = ['title', 'replace_value', 'tag']