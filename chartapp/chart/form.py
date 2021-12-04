from django import forms
from .models import Subject

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'
        widgets = {
            'label': forms.TextInput(),
            'target': forms.TextInput(),
            'policy': forms.TextInput(),
            'practice': forms.TextInput()
        }