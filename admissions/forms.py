from django import forms
from .models import StudentApplication

from django import forms
from django.core.exceptions import ValidationError
from .models import StudentApplication
from PIL import Image

MAX_PHOTO_SIZE_MB = 2
MAX_SIGNATURE_SIZE_MB = 1
MAX_DOCUMENT_SIZE_MB = 5

ALLOWED_IMAGE_TYPES = ['image/jpeg', 'image/png']
ALLOWED_DOC_TYPES = ['application/pdf']

MAX_PHOTO_DIMENSIONS = (600, 600)
MAX_SIGNATURE_DIMENSIONS = (400, 200)

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
            'signature': forms.ClearableFileInput(attrs={'class': 'form-input'}),
            'document': forms.ClearableFileInput(attrs={'class': 'form-input'}),
        }

    def clean_photo(self):
        photo = self.cleaned_data.get('photo')
        if photo:
            if photo.size > MAX_PHOTO_SIZE_MB * 1024 * 1024:
                raise ValidationError(f"Photo size should not exceed {MAX_PHOTO_SIZE_MB}MB.")
            if photo.content_type not in ALLOWED_IMAGE_TYPES:
                raise ValidationError("Only JPEG or PNG images are allowed for photo.")
            img = Image.open(photo)
            if img.size[0] > MAX_PHOTO_DIMENSIONS[0] or img.size[1] > MAX_PHOTO_DIMENSIONS[1]:
                raise ValidationError(f"Photo dimensions should not exceed {MAX_PHOTO_DIMENSIONS[0]}x{MAX_PHOTO_DIMENSIONS[1]} pixels.")
        return photo

    def clean_signature(self):
        signature = self.cleaned_data.get('signature')
        if signature:
            if signature.size > MAX_SIGNATURE_SIZE_MB * 1024 * 1024:
                raise ValidationError(f"Signature size should not exceed {MAX_SIGNATURE_SIZE_MB}MB.")
            if signature.content_type not in ALLOWED_IMAGE_TYPES:
                raise ValidationError("Only JPEG or PNG images are allowed for signature.")
            img = Image.open(signature)
            if img.size[0] > MAX_SIGNATURE_DIMENSIONS[0] or img.size[1] > MAX_SIGNATURE_DIMENSIONS[1]:
                raise ValidationError(f"Signature dimensions should not exceed {MAX_SIGNATURE_DIMENSIONS[0]}x{MAX_SIGNATURE_DIMENSIONS[1]} pixels.")
        return signature

    def clean_document(self):
        document = self.cleaned_data.get('document')
        if document:
            if document.size > MAX_DOCUMENT_SIZE_MB * 1024 * 1024:
                raise ValidationError(f"Document size should not exceed {MAX_DOCUMENT_SIZE_MB}MB.")
            if document.content_type not in ALLOWED_DOC_TYPES:
                raise ValidationError("Only PDF files are allowed.")
        return document



class StudentLoginForm(forms.Form):
    email = forms.EmailField(required=False, label="Email (optional)")
    student_id = forms.CharField(required=False, label="Student ID (optional)")
    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label="Date of Birth")


