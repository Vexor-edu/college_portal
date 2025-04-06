from django import forms
from .models import StudentApplication

class StudentApplicationForm(forms.ModelForm):
    class Meta:
        model = StudentApplication
        fields = '__all__'
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'Your full name', 'class': 'form-input'}),
            'father_name': forms.TextInput(attrs={'placeholder': 'Your father\'s name', 'class': 'form-input'}),
            'dob': forms.DateInput(attrs={'type': 'date', 'class': 'form-input'}),
            'email': forms.EmailInput(attrs={'placeholder': 'email@example.com', 'class': 'form-input'}),
            'phone': forms.TextInput(attrs={'placeholder': 'e.g. 9876543210', 'class': 'form-input'}),
            'address': forms.Textarea(attrs={'placeholder': 'Your full address', 'class': 'form-textarea'}),
            'course': forms.Select(attrs={'class': 'form-select'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-input'}),
            'document': forms.ClearableFileInput(attrs={'class': 'form-input'}),
            'signature': forms.ClearableFileInput(attrs={'class': 'form-input'}),
        }
