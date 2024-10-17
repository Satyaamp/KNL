from django.shortcuts import render,HttpResponse , redirect
from.models import Registration



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

def book(request):
    return render(request, 'book.html')

def sitemap(request):
    return render(request,'sitemap.html')

def login(request):
    return render(request,'login.html')


def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('confirmation')
    else:
        form = RegistrationForm()
    return render(request, 'registration/form.html', {'form': form})

def confirmation_view(request):
    return render(request, 'registration/confirmation.html')



