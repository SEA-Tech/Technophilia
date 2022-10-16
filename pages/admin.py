from django.contrib import admin
from .models import Hospital, Donor, BloodBank, HospitalDonation, HospitalUse, DonationRequest

# Register your models here.
admin.site.register(Hospital)
admin.site.register(Donor)
admin.site.register(BloodBank)
admin.site.register(HospitalDonation)
admin.site.register(HospitalUse)
admin.site.register(DonationRequest)