from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = [
            'customer_name', 'customer_email', 'customer_phone',
            'reservation_date', 'reservation_time', 'num_guests',
            'table_number', 'special_request',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['customer_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Your Name'})
        self.fields['customer_email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Your Email'})
        self.fields['customer_phone'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Your Phone'})
        self.fields['reservation_date'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Reservation Date'})
        self.fields['reservation_time'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Reservation Time'})
        self.fields['num_guests'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Number of Guests'})
        self.fields['table_number'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Table Number'})
        self.fields['special_request'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Special Requests'})
