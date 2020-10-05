from django import forms
from .models import Staff

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ('email', 'password', 'name', 'can_login',)

    password = forms.CharField(widget=forms.PasswordInput)