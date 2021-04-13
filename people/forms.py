from django import forms
from .models import Visitor,UnknownVisitor


class VisitorForm(forms.ModelForm):
    class Meta:
        model = Visitor
        fields = "__all__"

        widgets = {
            'name':forms.Select(attrs={'class':'form__input-scroll'}),
            'temp':forms.NumberInput(attrs={'class':'form__input','placeholder':'Temperature'})
        }

class UnknownVisitor(forms.ModelForm):
    class Meta:
        model = UnknownVisitor
        fields = "__all__"

        widgets = {
            'name':forms.TextInput(attrs={'class':'form__input','placeholder':'Name','autocomplete':'off'}),
            'temp':forms.NumberInput(attrs={'class':'form__input','placeholder':'Temperature'})
        }