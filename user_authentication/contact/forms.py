from contact.models import ContactMessage
from django import forms
__author__ = 'narcis'

class ContactForm(forms.ModelForm):

    class Meta:
        model=ContactMessage
        fields=['title','email','content']