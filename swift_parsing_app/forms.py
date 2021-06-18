from django import forms
from django.core.validators import FileExtensionValidator
from .models import SourceFile


class FileFieldForm(forms.Form):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}),
                                 validators=[FileExtensionValidator(allowed_extensions='csv')])

    def __init__(self, *args, **kwargs):
        super(FileFieldForm, self).__init__(*args, **kwargs)
        # self.initial['topic'] = 'Choose Topic'
        self.fields['file_field'].widget.attrs['class'] = "form-control"
        # self.fields['investigation_result'].widget.attrs['class'] = "form-control"
