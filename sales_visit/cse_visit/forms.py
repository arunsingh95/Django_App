from django import forms
from .models import *


class CustomerEditForm(forms.ModelForm):

    class Meta:
        model = CustomerVisitDetails
        fields = ('attachment',)
