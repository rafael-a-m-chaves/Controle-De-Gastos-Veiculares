from django import forms
from login.models import Veiculos, MyUser
from django.contrib.auth.models import User

class CadForm (forms.ModelForm):
    class Meta:
        model = Veiculos
        fields = ('placa', 'veiculo', 'Atualkm')


