from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """Create a model form with a meta class for the contact form. All fields should be required. Additionally
    they should all have no labels for a cleaner UI and pass through a placeholder and form-control class."""

    # Create Meta Class
    class Meta:
        model = Contact
        fields = ['contact_title', 'contact_body', 'email']

    # Details fields for the contact form
    contact_title = forms.CharField(
        required=True,
        label='',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Title'
        })
    )

    contact_body = forms.CharField(
        required=True,
        label='',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Message'
        })
    )

    email = forms.EmailField(
        required=True,
        label='',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email'
        })
    )

