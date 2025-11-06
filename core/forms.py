from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):

    first_name = forms.CharField(label='Primeiro Nome', max_length=30, required=True)
    last_name = forms.CharField(label='Sobrenome', max_length=30, required=True)
    phone = forms.CharField(label='Telefone', max_length=15, required=True)
    cpf = forms.CharField(label='CPF', max_length=14, required=True)
    sex = forms.ChoiceField(label='Sexo', choices=[('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outro')], required=True)
    birth_date = forms.DateField(label='Data de Nascimento', required=True, widget=forms.DateInput(attrs={'type': 'date'}))
    email = forms.EmailField(label='Email', required=True)
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'phone', 'cpf', 'sex', 'birth_date', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Este email já está em uso.")
        return email