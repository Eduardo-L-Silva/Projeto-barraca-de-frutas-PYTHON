from django import forms
from django.contrib.auth.models import User
from .models import Fruta

class FrutaForm(forms.ModelForm):
    class Meta:
        model = Fruta
        fields = ['nome', 'classificacao', 'fresca', 'quantidade', 'valor']

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']  # Adicione outros campos conforme necessário
        widgets = {
            'password': forms.PasswordInput(),  # Use um campo de senha
        }
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

class EditFrutaForm(forms.ModelForm):
    class Meta:
        model = Fruta
        fields = ['nome', 'classificacao', 'fresca', 'quantidade', 'valor']


class VendedorForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }