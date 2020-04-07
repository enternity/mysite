from django import forms

class ContactForm(forms.Form):
    """
        Form contact with admin website
    """
    fullname = forms.CharField(label='name', max_length=25)
    email = forms.EmailField(label='email', max_length=121)
    message = forms.CharField(widget=forms.Textarea)        