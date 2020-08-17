from django.forms import ModelForm
from myfirstapp.models import Amount

class AmountForm(ModelForm):

    class Meta:
        model=Amount
        fields = ['amount']
        