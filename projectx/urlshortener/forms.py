from django import forms

from .models import Short


class ShortForm(forms.ModelForm):
    
    full_url = forms.URLField(
        widget=forms.URLInput(
            attrs={
                "class": "form-control form-control-lg", 
                "placeholder": "Your URL to shorten"
            }
        )
    )
    
    class Meta:
        model = Short
        fields = ['full_url', 'short_url']