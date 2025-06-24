from django import forms
from .models import Student
from datetime import date

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'roll',
            'name',
            'gender',
            'branch',
            'year_of_study',
            'email',
            'phone_number',
            'date_of_birth',
            'address',
            'guardian_name',
            'guardian_phone',
        ]
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'address': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'admission_date': forms.DateInput(attrs={'type': 'date'}),
            'roll_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'branch': forms.TextInput(attrs={'class': 'form-control'}),
            'year_of_study': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'guardian_name': forms.TextInput(attrs={'class': 'form-control'}),
            'guardian_phone': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add placeholders and classes if needed
        self.fields['roll'].widget.attrs.update({'class': 'form-control'})
        self.fields['name'].widget.attrs.update({'class': 'form-control'})

    def clean_date_of_birth(self):
        """Additional form-level validation for date of birth"""
        dob = self.cleaned_data['date_of_birth']
        if dob > date.today():
            raise forms.ValidationError("Date of birth cannot be in the future")
        return dob