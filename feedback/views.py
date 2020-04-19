from django.shortcuts import render, redirect
from . import forms
from .models import FeedBack


def feedback(request):
    
    if request.method == 'POST':
        form = forms.FeedBack(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print("User feedback: ")
            print(f"{data['name'], data['email'], data['message']}")
            feedback = FeedBack(name=data['name'], email=data['email'], message=data['message'])
            feedback.save()
            
            return render(request, template_name='thankyou.html')
    
    return render(request, template_name='404error.html')
