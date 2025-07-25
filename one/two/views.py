from django.shortcuts import render,HttpResponse , redirect
# from.models import RegistrationForm
from .forms import RegistrationForm 



# Create your views here.
def index(request):
    return render(request, 'index.html')
    # return HttpResponse("this is the homepage")
def  about(request):
    return render(request, 'about.html')
    #  return HttpResponse("this is the about page")
 
def services(request):
    return render(request, 'services.html')
    #  return HttpResponse("this is the service page")
def contact(request):
    return render(request, 'contact.html')
    #  return HttpResponse("this is the conatct page")
    
def terms(request):
    return render(request, 'terms.html')

def privacy(request):
    return render(request, 'privacy.html')

def faq(request):
    return render(request, 'faq.html')

def feedback(request):
    return render(request, 'feedback.html')


def complaint(request):
    return render(request, 'complaint.html')


def suggestion(request):
    return render(request, 'suggestion.html')

from django.contrib.auth.models import User
from .models import Registration

def book(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            username = form.cleaned_data['contact'] or form.cleaned_data['aadhar_number']
            if User.objects.filter(username=username).exists():
                form.add_error('contact', 'A user with this contact number already exists.')
                return render(request, 'registration.html', {'form': form})
            if Registration.objects.filter(aadhar_number=form.cleaned_data['aadhar_number']).exists():
                form.add_error('aadhar_number', 'A user with this Aadhaar number already exists.')
                return render(request, 'registration.html', {'form': form})
            registration = form.save(commit=False)
            password = form.cleaned_data['aadhar_number']
            user = User.objects.create_user(username=username, password=password, email=form.cleaned_data.get('email', ''))
            print(f"Created user: {user} with username: {user.username}")
            registration.user = user
            registration.save()
            print(f"Saved registration: {registration} with user {user}")
            return render(request, 'thank_you.html', {'name': form.cleaned_data['name']})
        else:
            print(f"Form errors: {form.errors}")
    else:
        form = RegistrationForm()
    return render(request, 'registration.html', {'form': form})


def sitemap(request):
    return render(request,'sitemap.html')

from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from django.contrib.auth import logout

def logout_redirect(request):
    return render(request, 'logout_redirect.html')

def custom_logout(request):
    logout(request)
    return render(request, 'logout_redirect.html')

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('/')  # Redirect to homepage or dashboard
            else:
                form.add_error(None, 'Invalid credentials or Something Went Wrong!')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def profile(request):
    registration = None
    if hasattr(request.user, 'registration'):
        registration = request.user.registration
    print(f"Profile view: registration = {registration}")
    context = {}
    if registration:
        context = {
            'name': registration.name,
            'contact': registration.contact,
            'fathers_name': registration.fathers_name,
            'aadhar_number_last4': registration.aadhar_number[-4:] if registration.aadhar_number else '',
            'pic_url': registration.pic.url if registration.pic else '',
            'aadhar_pic_url': registration.aadhar_pic.url if hasattr(registration, 'aadhar_pic') and registration.aadhar_pic else '',
            'seat_number': registration.seat_number,
            'batch': registration.batch,
        }
    print(f"Profile view: context = {context}")
    return render(request, 'profile_custom.html', context)


def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            # You can handle the data or save it
            # For now, just return a thank you page
            return render(request, 'thank_you.html', {'name': form.cleaned_data['name']})
    else:
        form = RegistrationForm()
    return render(request, 'registration.html', {'form': form})



