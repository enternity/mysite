from django import forms

class FeedBack(forms.Form):
    """
        Form feedback with admin website
    """
    name = forms.CharField(label='name', max_length=25)
    email = forms.EmailField(label='email', max_length=121)
    message = forms.CharField(widget=forms.Textarea)

    def __str__(self):
        return f"{self.name}({self.email})"        