from django import forms
from .models import Order


class MakePaymentForm(forms.Form):

    MONTH_CHOICES = [(i, i) for i in range(1, 13)]
    YEAR_CHOICES = [(i, i) for i in range(2020, 2036)]

    credit_card_number = forms.CharField(
        required=False,
        label="",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Credit Card Number'
        })
    )

    cvv = forms.CharField(
        required=False,
        label="",
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'CVV'
        })
    )

    expiry_month = forms.ChoiceField(
        choices=MONTH_CHOICES,
        required=False,
        label="",
        widget=forms.Select(attrs={
            'class': 'form-control',
        })
    )

    expiry_year = forms.ChoiceField(
        choices=YEAR_CHOICES,
        required=False,
        label="",
        widget=forms.Select(attrs={
            'class': 'form-control',
        })
    )

    stripe_id = forms.CharField(
        widget=forms.HiddenInput
    )


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'phone_number', 'country', 'postcode', 'town_or_city', 'street_address1',
                  'street_address2', 'county')

    full_name = forms.CharField(
        required=True,
        label="",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Full Name'
        })
    )

    phone_number = forms.CharField(
        required=True,
        label="",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Phone Number'
        })
    )

    country = forms.CharField(
        required=True,
        label="",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Country'
        })
    )

    postcode = forms.CharField(
        required=True,
        label="",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Postcode'
        })
    )

    town_or_city = forms.CharField(
        required=True,
        label="",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Town or City'
        })
    )

    street_address1 = forms.CharField(
        required=True,
        label="",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Street Address Line 1'
        })
    )

    street_address2 = forms.CharField(
        required=True,
        label="",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Street Address Line 2'
        })
    )

    county = forms.CharField(
        required=True,
        label="",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'County'
        })
    )
