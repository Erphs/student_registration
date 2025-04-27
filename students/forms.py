from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email', ]  # courses اضافه شد
        widgets = {
            'courses': forms.CheckboxSelectMultiple()
        }

