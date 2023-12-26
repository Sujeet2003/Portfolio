from django.shortcuts import render, redirect
from .models import ContactUs
from django.contrib import messages

def home(request):
    testinomials = ContactUs.objects.filter()[0:2]
    # test = testinomials.order_by('created_date')
    name = {
        'title': 'Home_Page',
        'testinomials': testinomials,
    }
    return render(request, 'home.html', name)
def skills(request):
    name = {
        'title': 'Skills_Page',
    }
    return render(request, 'skills.html', name)
def projects(request):
    name = {
        'title': 'Project_Page',
    }
    return render(request, 'project.html', name)
def academics(request):
    name = {
        'title': 'Academics_Page',
    }
    return render(request, 'academic.html', name)
def contact(request):
    dict_values = {
        'title': 'Contact_Page',
    }
    if request.method == 'POST':
        contactus = ContactUs()
        contactus.name = request.POST['name']
        contactus.phone = request.POST['phone']
        contactus.email = request.POST['email']
        contactus.description = request.POST['description']
        contactus.save()
        messages.success(request, "Submitted successfully!!")
        return redirect('contact')
    else:
        return render(request, 'contact.html', dict_values)