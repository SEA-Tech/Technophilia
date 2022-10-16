from django.shortcuts import render, redirect
from .models import Hospital, Donor, HospitalDonation, HospitalUse, DonationRequest
from accounts.models import CustomUser
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate

# Create your views here.

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username (or) Password is incorrect')

    context = {}
    return render(request, 'pages/login.html', context)

def logoutUser(request):
    if not request.user.is_authenticated:
        return redirect('home')
    messages.success(request, f'{request.user} has been succesfully logged out.')
    logout(request)
    return redirect('login')


def home(request):
    context = {}
    return render(request, 'pages/home.html', context)


def hospitals(request):
    hospital_list = Hospital.objects.all()
    context = {'hospitals': hospital_list}
    return render(request, 'pages/hospitals.html', context)


def register_hospital(request):
    if request.user.is_superuser:
        return redirect('home')
    if request.method == 'POST':
        name = request.POST.get('name')
        contact = request.POST.get('contact')
        address = request.POST.get('address')
        pincode = request.POST.get('pincode')
        city = request.POST.get('city')
        country = request.POST.get('country')

        hospital = Hospital(name=name, contact=contact, address=address, pincode=pincode, city=city, country=country)
        hospital.save()
        return redirect('home')

    context = {}
    return render(request, 'pages/register-hospital.html', context)


def hospital_page(request, id):
    if not request.user.is_authenticated:
        return redirect('login')
    hospital = Hospital.objects.get(id=id)
    context = {'hospital': hospital}
    return render(request, 'pages/hospital-page.html', context)


def donors_list(request, hospital_id):
    if not request.user.is_authenticated:
        return redirect('login')
    hospital = Hospital.objects.get(id=hospital_id)
    donors = Donor.objects.filter(hospital=hospital)
    context = {'donors': donors, 'name': hospital.name}
    return render(request, 'pages/donor-list.html', context)


def register_donation(request, hospital_id):
    if not request.user.is_authenticated:
        return redirect('login')
    hospital = Hospital.objects.get(id=hospital_id)
    if request.method == 'POST':
        username = request.POST.get('username')
        donor = CustomUser.objects.get(username=username)
        blood_group = donor.blood_group
        if blood_group == 'A RhD positive (A+)':
            hospital.ap += 1
        elif blood_group == 'A RhD negative (A-)':
            hospital.an += 1
        elif blood_group == 'B RhD positive (B+)':
            hospital.bp += 1
        elif blood_group == 'B RhD negative (B-)':
            hospital.bn += 1
        elif blood_group == 'O RhD positive (O+)':
            hospital.op += 1
        elif blood_group == 'O RhD negative (O-)':
            hospital.on += 1
        elif blood_group == 'AB RhD positive (AB+)':
            hospital.abp += 1
        elif blood_group == 'AB RhD negative (AB-)':
            hospital.abn += 1
        hospital.save()
        donation = HospitalDonation(donor=donor, hospital=hospital)
        donation.save()
        return redirect('home')
    context = {'hospital': hospital}
    return render(request, 'pages/register-donation.html', context)


def use_blood_hospital(request, hospital_id):
    if not request.user.is_authenticated:
        return redirect('login')
    hospital = Hospital.objects.get(id=hospital_id)
    if request.method == 'POST':
        blood_group = request.POST.get('blood_group')
        if blood_group == 'A RhD positive (A+)':
            hospital.ap -= 1
        elif blood_group == 'A RhD negative (A-)':
            hospital.an -= 1
        elif blood_group == 'B RhD positive (B+)':
            hospital.bp -= 1
        elif blood_group == 'B RhD negative (B-)':
            hospital.bn -= 1
        elif blood_group == 'O RhD positive (O+)':
            hospital.op -= 1
        elif blood_group == 'O RhD negative (O-)':
            hospital.on -= 1
        elif blood_group == 'AB RhD positive (AB+)':
            hospital.abp -= 1
        elif blood_group == 'AB RhD negative (AB-)':
            hospital.abn -= 1
        hospital.save()
        usage = HospitalUse(hospital=hospital, blood_group=blood_group)
        usage.save()
        return redirect('home')
    context = {'hospital': hospital}
    return render(request, 'pages/register-usage.html', context)


def donation_requests(request):
    if not request.user.is_authenticated:
        return redirect('login')
    requests = DonationRequest.objects.filter(satisfied=False)
    context = {'requests': requests}
    return render(request, 'pages/donation-request.html', context)


def search_for_blood(request):
    context = {}
    return render(request, 'pages/search-blood.html', context)
    

def search_for_blood_result(request, blood_group):
    hospitals = Hospital.objects.all()
    if blood_group == 'ap':
        hospitals = hospitals.filter(ap__gt=0)
    elif blood_group == 'an':
        hospitals = hospitals.filter(an__gt=0)
    elif blood_group == 'bp':
        hospitals = hospitals.filter(bp__gt=0)
    elif blood_group == 'bn':
        hospitals = hospitals.filter(bn__gt=0)
    elif blood_group == 'op':
        hospitals = hospitals.filter(op__gt=0)
    elif blood_group == 'on':
        hospitals = hospitals.filter(on__gt=0)
    elif blood_group == 'abp':
        hospitals = hospitals.filter(abp__gt=0)
    elif blood_group == 'abn':
        hospitals = hospitals.filter(abn__gt=0)

    context = {'hospitals': hospitals}
    return render(request, 'pages/blood-results.html', context)