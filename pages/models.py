from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from accounts.models import CustomUser

# Create your models here.
class Hospital(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    contact = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    pincode = models.PositiveIntegerField()
    city = models.CharField(max_length=125, default='')
    country = models.CharField(max_length=125)
    op = models.IntegerField(default=0)
    on = models.IntegerField(default=0)
    ap = models.IntegerField(default=0)
    an = models.IntegerField(default=0)
    bp = models.IntegerField(default=0)
    bn = models.IntegerField(default=0)
    abp = models.IntegerField(default=0)
    abn = models.IntegerField(default=0)
    image = models.ImageField(null=True, blank=True)

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url=''
        return url

    def __str__(self):
        return self.name


class BloodBank(models.Model):
    name = models.CharField(max_length=255, unique=True)
    contact = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    pincode = models.PositiveIntegerField()
    city = models.CharField(max_length=125, default='')
    country = models.CharField(max_length=125)
    def __str__(self):
        return self.name
    
class Donor(models.Model):

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

    name = models.CharField(max_length=255)
    aadhar_no = models.CharField(max_length=15)
    age = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(70)])
    address = models.CharField(max_length=255)
    blood_group = models.TextField(choices=blood_groups)
    approved = models.BooleanField(default=False)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, null=True)
    time_of_donation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class HospitalDonation(models.Model):
    donor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, null=True)
    time_of_donation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.donor.username + '-' + str(self.time_of_donation)


class HospitalUse(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    blood_group = models.CharField(max_length=50)
    time_of_use = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.hospital.name + '-' + str(self.time_of_use)

class DonationRequest(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
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
    blood_group = models.CharField(choices=blood_groups, max_length=50)
    satisfied = models.BooleanField(default=False)
    time_of_request = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.hospital + '-' + str(self.time_of_request)
    