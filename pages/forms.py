from django import forms
from .models import Hospital, Donor
from accounts.models import CustomUser

class DonorForm(forms.ModelForm):
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

    name = forms.CharField(max_length=255)
    aadhar_no = forms.CharField(max_length=15)
    address = forms.CharField(max_length=255)
    blood_group = forms.TextField(choices=blood_groups)
    approved = forms.BooleanField(default=False)
    hospital = forms.ModelChoiceField(queryset=Hospital.objects.all())

    class Meta:
        model = Donor
        fields = '__all__'
