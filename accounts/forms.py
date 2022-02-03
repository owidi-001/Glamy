from django import forms
from .models import User
from django.core.exceptions import ValidationError
from .validators import phone_number_validator, email_validator


class UserCreationForm(forms.ModelForm):
    email = forms.EmailField(help_text="Email is required")
    phone = forms.CharField(max_length=13, help_text="Phone number is required")

    class Meta:
        model = User
        fields = ["email", "phone", "password"]

    def clean_email(self):
        email = self.cleaned_data.get("email")

        if not email:
            raise ValidationError("Please provide your email address")

        if not email_validator(email):
            raise ValidationError("please provide a valid Email address")
        return email

    def clean_phone(self):
        phone_no = self.cleaned_data.get("phone_number")

        if not phone_no:
            raise ValidationError("please provide your phone number")

        if not phone_number_validator(phone_no):
            raise ValidationError(
                "please provide valid phone number eg +254712345678")
        return phone_no

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class UserLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=150, widget=forms.PasswordInput)
