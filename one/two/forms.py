from django import forms
from .models import Registration

class LoginForm(forms.Form):
    username = forms.CharField(label='Phone Number or Aadhaar Number', max_length=20)
    password = forms.CharField(label='Aadhaar Number', widget=forms.PasswordInput)

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['name', 'contact', 'fathers_name', 'aadhar_number', 'address', 'pic', 'aadhar_pic', 'batch']
        labels = {
            'name': 'Full Name',
            'contact': 'Contact Number',
            'fathers_name': "Father's Name",
            'aadhar_number': 'Aadhaar Number',
            'address': 'Address',
            'pic': 'Your Photo',
            'aadhar_pic': 'Aadhaar Photo',
            'batch': 'Shift',
        }
