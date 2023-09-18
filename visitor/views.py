# visitor/views.py
from django.shortcuts import render, redirect
from .forms import VisitorLoginForm
from .models import Visitor
from django.core.mail import send_mail

def login_visitor(request):
    if request.method == 'POST':
        form = VisitorLoginForm(request.POST)
        
        if form.is_valid():
            email = form.cleaned_data['email']
            person_to_visit = form.cleaned_data['person_to_visit']
            staff_email = person_to_visit.email
            visitor, created = Visitor.objects.get_or_create(email=email, person_to_visit=person_to_visit)
            send_mail(
                'Staff has been Notified',
                'Staff will come to see you soon',
                'balaydalakay@gmail.com',
                [staff_email],
                fail_silently=False
            )
            return redirect('welcome')
    else:
        form = VisitorLoginForm()
    return render(request, 'visitor/login.html', {'form': form})

def welcome(request):
    return render(request, 'visitor/welcome.html')
