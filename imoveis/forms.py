from django import forms

from .models import Anuncio
from .validators import validate_category


class AnuncioCreateForm(forms.ModelForm):
    class Meta:
        model = Anuncio
        fields = [
            'name',
            'cidade',
            'transacao',
            'tipo',
            'quartos',
            'banheiros',
            'vagas',
            'slug',
        ]

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if name == "Hello":
            raise forms.ValidationError("Not a valid name")
        return name

    # def clean_email(self):
    #     email = self.cleaned_data.get("email")
    #     if ".edu" in email:
    #         raise forms.ValidationError("We do not accept edu emails")
    #     return email