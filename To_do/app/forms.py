from django import forms

from.models import To_do

class ToForm(forms.ModelForm):
    class Meta:
        model = To_do
        fields = '__all__'