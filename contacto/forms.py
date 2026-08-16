from django import forms
from .models import MensajeEditorial


class ContactoForm(forms.ModelForm):
    class Meta:
        model = MensajeEditorial
        fields = ["nombre", "correo", "asunto", "mensaje"]
        widgets = {
            "nombre": forms.TextInput(attrs={
                "class": "bev-form-input",
                "placeholder": "Tu nombre",
                "required": True,
            }),
            "correo": forms.EmailInput(attrs={
                "class": "bev-form-input",
                "placeholder": "tu@correo.com",
                "required": True,
            }),
            "asunto": forms.TextInput(attrs={
                "class": "bev-form-input",
                "placeholder": "¿En qué podemos ayudarte?",
            }),
            "mensaje": forms.Textarea(attrs={
                "class": "bev-form-input",
                "placeholder": "Escribe tu mensaje aquí...",
                "rows": 5,
                "required": True,
            }),
        }