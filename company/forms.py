from django.forms import fields
from company.models import CrudOperation
from django import forms
from company.models import CrudOperation
from django.forms import fields


class CrudForm(forms.ModelForm):  # extending ModelForm, not Form as before
        class Meta:
            model = CrudOperation
            fields = ['name','email']



