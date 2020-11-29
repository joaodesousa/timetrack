from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from .models import Servico, Timesheet
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms.models import ModelForm
from django.forms.widgets import CheckboxSelectMultiple, Select, SelectMultiple, NullBooleanSelect, RadioSelect, CheckboxInput
from django.forms import TextInput
from django.conf import settings


CARRO = (
    (0,"Unidade Móvel (NZ)"),
    (1,"Unidade Móvel (SM)"),
    (2,"Unidade Móvel (TP)"),
    (3,"Unidade Móvel (UN)"),
    (4,"Unidade Móvel (XH)"),
    (5,"Carro Próprio"),
)

class CriarNovo(ModelForm):
    class Meta:
        model = Timesheet
        fields = '__all__'
        data = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)

    def __init__(self, *args, **kwargs):
        
        super(CriarNovo, self).__init__(*args, **kwargs)
        
        self.fields["servico"].widget = SelectMultiple(attrs={'class': 'form-control'})
        self.fields["servico"].queryset = Servico.objects.all()
        self.fields['entrada'].widget = TextInput(attrs={'class': 'form-control', 'placeholder': 'HH:MM'})
        self.fields['saida'].widget = TextInput(attrs={'class': 'form-control', 'placeholder': 'HH:MM'})
        self.fields['almoco'].widget = TextInput(attrs={'class': 'form-control', 'placeholder': 'HH:MM'})
        self.fields['almoco_fim'].widget = TextInput(attrs={'class': 'form-control', 'placeholder': 'HH:MM'})
        self.fields['zona'].widget = TextInput(attrs={'class': 'form-control'})
        self.fields['medico'].widget = TextInput(attrs={'class': 'form-control'})
        self.fields['carro'].widget = Select(choices=CARRO, attrs={'class': 'form-control'})


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'password1', 'password2']

class PrettyAuthenticationForm(AuthenticationForm):
    class Meta:
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'})
        }
