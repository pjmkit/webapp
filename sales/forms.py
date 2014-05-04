from django import forms
from django.core.exceptions import ValidationError

from .models import SellTransaction
from .models import SellTransactionDtl

class SellTransactionUpdateForm(forms.ModelForm):
    
    class Meta:
        model = SellTransaction
        fields = ("organisation_id", "invoice_number")
     