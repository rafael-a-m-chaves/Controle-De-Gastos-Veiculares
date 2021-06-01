from django import forms
from login.models import Veiculos


class CadForm (forms.ModelForm):
    class Meta:
        model = Veiculos
        fields = ('placa', 'veiculo', 'Atualkm')


   