from django import forms
from login.models import Veiculos
from django.contrib.auth.models import User

class CadForm (forms.ModelForm):
    class Meta:
        model = Veiculos
        fields = ('placa', 'veiculo', 'Atualkm')


   