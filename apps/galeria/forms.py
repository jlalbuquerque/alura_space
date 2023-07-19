from django import forms
from apps.galeria.models import Fotografia
from captcha.fields import ReCaptchaField

class FotografiaForms(forms.ModelForm):
    class Meta:
        model = Fotografia
        exclude = ['publicada',]
        labels = {
            'descricao': 'Descrição',
            'data_fotografia': 'Data de registro',
            'usuario': 'Usuário',
        }
        
        
        fields = {
            'nome': forms.CharField(required = True),
            'legenda': forms.CharField(required = True),
            'categoria': forms.CharField(required = True),
            'descricao': forms.CharField(required = True),
            'foto': forms.ImageField(required = True),
            'data_fotografia': forms.ImageField(required = True),
            'usuario': forms.CharField(required = True),
        }
        
        widgets = {
            'nome': forms.TextInput(attrs={'class':'form-control'}),
            'legenda': forms.TextInput(attrs={'class':'form-control'}),
            'categoria': forms.Select(attrs={'class':'form-control'}),
            'descricao': forms.Textarea(attrs={'class':'form-control'}),
            'foto': forms.FileInput(attrs={'class':'form-control'}),
            'data_fotografia': forms.DateInput(
                attrs={
                    'class':'form-control',
                    'type': 'date',
                },

                format='%d/%m/%Y'
            ),
            'usuario': forms.Select(attrs={'class':'form-control'}),
        }
    
    
    captcha = ReCaptchaField()