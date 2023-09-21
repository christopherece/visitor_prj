# visitor/views.py
from django.shortcuts import render, redirect
from .forms import VisitorLoginForm
from .models import Visitor
from django.core.mail import send_mail

def dashboard(request):
    return render(request, 'visitor/dashboard.html')

def login_visitor(request):
    if request.method == 'POST':
        form = VisitorLoginForm(request.POST)
        
        if form.is_valid():
            # email = form.cleaned_data['email']
            name = form.cleaned_data['name']
            person_to_visit = form.cleaned_data['person_to_visit']
            staff_email = person_to_visit.email
            visitor, created = Visitor.objects.get_or_create(name=name, person_to_visit=person_to_visit)
            send_mail(
                'You Have a Visitor',
                name + ' is waiting for you at the Reception.',
                'balaydalakay@gmail.com',
                [staff_email, 'christopheranchetaece@gmail.com'],
                fail_silently=False
            )
            return render(request, 'visitor/welcome.html', {'name': name})
    else:
        form = VisitorLoginForm()
    return render(request, 'visitor/login.html', {'form': form})

def welcome(request):
    return render(request, 'visitor/welcome.html')
