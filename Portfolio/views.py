from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

def home(request):
    name = {
        'title': 'Home_Page',
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
    values = {}
    dict_values = {
        'title': 'Contact_Page',
        'data': values,
    }
    try:
        if request.method == 'POST':
            name = request.GET['name']
            phone = request.GET['phone']
            email = request.GET['email']
            description = request.GET['description']
            values = {
                'name': name,
                'phone': phone,
                'email': email,
                'description': description,
            }
    except:
        pass
    return render(request, 'contact.html', dict_values)