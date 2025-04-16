from django import forms
from .models import Newsletter, Subscriber
from django_ckeditor_5.widgets import CKEditor5Widget

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['title', 'description']

class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']

class EmailForm(forms.Form):
    subject = forms.CharField(max_length=255)
    message = forms.CharField(widget=CKEditor5Widget(config_name='default'))
    