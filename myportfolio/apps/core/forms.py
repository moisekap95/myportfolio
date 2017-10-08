from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Name', widget=forms.TextInput(attrs={'placeholder': 'Please Enter your Name *'}), required=True)
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'placeholder': 'Please Enter your Email *'}), required=True)
    subject = forms.CharField(label='Subject', widget=forms.TextInput(attrs={'placeholder': 'Please Enter your Subject *'}), required=True)
    message = forms.CharField(label='Message', widget=forms.Textarea(attrs={'placeholder': 'Please Enter your message *'}), required=True)