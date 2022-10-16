from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class CustomUser(AbstractUser):
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

    aadhar_no = models.CharField(max_length=15, null=True)
    age = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(70)], null=True)
    address = models.CharField(max_length=255, null=True)
    blood_group = models.TextField(choices=blood_groups, null=True)

    def __str__(self):
        return self.username