from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.validators import MaxValueValidator, MinValueValidator
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    email = forms.EmailField()
    blood_groups = (
        ("A RhD positive (A+)", "A RhD positive (A+)"),
        ("A RhD negative (A-)", "A RhD negative (A-)"),
        ("B RhD positive (B+)", "B RhD positive (B+)"),
        ("B RhD negative (B-)", "B RhD negative (B-)"),
        ("O RhD positive (O+)", "O RhD positive (O+)"),
        ("O RhD negative (O-)", "O RhD negative (O-)"),
        ("AB RhD positive (AB+)", "AB RhD positive (AB+)"),
        ("AB RhD negative (AB-)", "AB RhD negative (AB-)")
    )

    aadhar_no = forms.CharField(max_length=15)
    age = forms.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(70)])
    address = forms.CharField(max_length=255)
    blood_group = forms.ChoiceField(choices=blood_groups)
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'aadhar_no', 'age', 'address', 'blood_group')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')