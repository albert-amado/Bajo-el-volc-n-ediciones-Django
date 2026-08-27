# noticias/forms.py
from django import forms
from .models import AlbumGaleria


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = [single_file_clean(data, initial)]
        return result


class AlbumAdminForm(forms.ModelForm):
    archivos_multiples = MultipleFileField(
        required=False,
        label="Subir múltiples archivos",
    )

    class Meta:
        model = AlbumGaleria
        fields = "__all__"