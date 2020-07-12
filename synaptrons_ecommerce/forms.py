from django import forms

class ContactForm(forms.Form):
    nome_completo = forms.CharField(
    error_messages={'required': 'Obrigatório o preenchimento do nome!'},
        widget=forms.TextInput(
            attrs={
        "class": "form-control",
        "placeholder": "Seu nome completo"
    }
)
    )
    email = forms.EmailField(
    error_messages={'required': 'Informe um email válido!'},
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Seu email"
        }
)
    )
    messagem = forms.CharField(
    error_messages={'required': 'Obrigatório o preenchimento do campo de mensagem!'},
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Sua mensagem"
            }
        )
    )
