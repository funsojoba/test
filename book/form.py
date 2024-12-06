"""

	•	Task: Create a form to register users with fields for:
	•	Username (required, unique).
	•	Email (required, valid format).
	•	Password (required, minimum 8 characters).
	•	Requirements:
	•	Use Django’s forms.Form or forms.ModelForm.
	•	Add custom validation for email to ensure it contains @example.com.
	•	Render the form in a simple HTML template.
	•	Expected Output: A working form with error messages displayed for invalid inputs.

"""

import re
from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib.auth.models import User


class UserRegistrationForm(forms.Form):
    username = forms.CharField(
        max_length=100, required=True, 
        label='Username', widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, min_length=8, required=True)
    
    def clean_username(self):
        username = self.clean_data.get("username")
        if User.objects.filter(username=username).exists():
            raise ValidationError("Username already exists")
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        # validate email with email regex
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_regex, email):
            raise ValidationError("Invalid email format")
        return email