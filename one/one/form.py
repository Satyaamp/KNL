from django import forms
from .models import Two

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = [
            'name', 'fathers_name', 'mothers_name', 'contact', 'address', 
            'pic', 'aadhar_number', 'aadhar_pic', 'batch', 'purpose', 'reference'
        ]
        widgets = {
            'batch': forms.Select(choices=[
                ('Batch 1', 'Batch 1'),
                ('Batch 2', 'Batch 2'),
                ('Batch 3', 'Batch 3'),
                ('Batch 4', 'Batch 4')
            ])
        }
