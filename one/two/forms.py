# forms.py
from django import forms

class StudentForm(forms.Form):
    candidateName = forms.CharField(label='Candidate Name', max_length=100)
    picture = forms.ImageField(label='Upload Your Picture')
    dob = forms.DateField(label='Enter D.O.B')
    gender = forms.ChoiceField(
        label='Gender',
        choices=[('male', 'Male'), ('female', 'Female'), ('notosat', 'Not to say'), ('default', 'Selected by Default')]
    )
    fatherName = forms.CharField(label="Father's Name", max_length=100)
    motherName = forms.CharField(label="Mother's Name", max_length=100, required=False)
    aadharNumber = forms.CharField(label='Candidate Aadhar Number', max_length=12)
    aadharFile = forms.FileField(label='Upload Aadhar')
    contactNumber = forms.CharField(label='Contact Number', max_length=10)
    email = forms.EmailField(label='Email Address')
    address = forms.CharField(label='Communication Address', widget=forms.Textarea)
    receipt = forms.FileField(label='Upload Registration Receipt/Proof')
