from django import forms

from wwwdj.models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ['date']
