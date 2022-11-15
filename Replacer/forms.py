from django import forms
from .models import ReplaceField, Template

class ReplaceFieldForm(forms.ModelForm):
    class Meta:
        model = ReplaceField
        fields = '__all__'

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'