from django.shortcuts import render, get_object_or_404, redirect
from django.template import RequestContext
from . import forms

def home(request):
    return render(request, 'homepage.html', {})


def contact(request):
    if request.method == 'POST':
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            pass
            #TO DO
                # Handle contact from user
    return render(request, 'contact.html')