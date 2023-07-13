from django import forms
from django.contrib.auth.models import User

class LoginForms(forms.Form):
    nome_login = forms.CharField(
        label='Nome de login',
        required=True,
        max_length=100,
        widget = forms.TextInput(
            attrs= {
                'class': 'form-control',
                'placeholder': 'Ex: João Silva'
            }
        )
    )
    senha_login = forms.CharField(
        label='Senha',
        required=True,
        max_length=70,
        widget = forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua senha'
            }
        )
    )

class CadastroForms(forms.Form):
    nome_cadastro = forms.CharField(
        label='Nome de Cadastro',
        max_length=100,
        required=True,
        widget = forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex: João Silva'
            }
        )
    )
    
    email = forms.CharField(
        label = 'Email de cadastro',
        max_length = 100,
        required = True,
        widget = forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex: eusoudemais@eusoudemais.com'
            }
        )
    )
    
    senha_1 = forms.CharField(
        label = 'Senha',
        max_length = 70,
        required = True,
        widget = forms.PasswordInput(
            attrs = {
                'class': 'form-control',
                'placeholder': 'Digite sua senha aqui:'
            }
        )
    )
    
    senha_2 = forms.CharField(
        label = 'Confirme sua senha',
        max_length = 70,
        required = True,
        widget = forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Confirme sua senha aqui:'
            }
        )
    )
    
    def clean_nome_cadastro(self):
        nome = self.cleaned_data.get('nome_cadastro')
        
        if nome:
            nome = nome.strip()
            if ' ' in nome:
                raise forms.ValidationError('Não é possível inserir espaços dentro do campo usuário!')
            elif User.objects.filter(username=nome).exists():
                raise forms.ValidationError('Usuário já existe!')
            else:
                return nome
    
    def clean_senha_2(self):
        if self.cleaned_data.get('senha_2') != self.cleaned_data.get('senha_2'):
            raise forms.ValidationError('As senhas não são iguais!')
        else:
            return self.cleaned_data.get('senha_2')
    
    def clean_email(self):
        if User.objects.filter(email=self.cleaned_data.get('email')).exists():
            raise forms.ValidationError('O email já existe')
        else:
            return self.cleaned_data.get('email')