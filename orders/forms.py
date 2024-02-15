from django import forms

from orders.models import Order


class OrderForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': 'John'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': 'Smith'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': "form-control", 'placeholder': 'you@example.com'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control",
                                                            'placeholder': 'USA, New York, St. Louisiana 12'}))

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address']
