from django.shortcuts import render, redirect
from . import forms
from . import models
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from edukom import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def homepage(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

from .forms import ContactForm
def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            data = form.save()
            subject = f'Message from {data.name}'
            html_message = render_to_string('emails/contact.html', {'data': data})
            from_email = settings.EMAIL_HOST_USER
            recipient_list = ['john@edukom.ng']
            message = EmailMessage(subject, html_message, from_email, recipient_list)
            message.content_subtype = 'html'
            message.send()
            messages.success(request, 'You message has been sent to the support team we will contact you soon.')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form':form})

def faq(request):
    return render(request, 'faq.html')


def succes_form(request, uid):
    guardian = models.Guardian.objects.get(uid=uid)
    guardian.full_name = f"{guardian.last_name} {guardian.first_name}"
    subject = 'Welcome to Edukom'
    html_message = render_to_string('emails/gaurdian_sucess.html', {'guardian': guardian})
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [guardian.email]
    message = EmailMessage(subject, html_message, from_email, recipient_list)
    message.content_subtype = 'html'

    admin_html_message = render_to_string('emails/guardiantoadmin.html', {'guardian': guardian})
    admin_from_email = settings.EMAIL_HOST_USER
    admin_recipient_list = ['john@edukom.ng']
    admin_message = EmailMessage(subject, admin_html_message, admin_from_email, admin_recipient_list)
    admin_message.content_subtype = 'html'
    
    mail = models.GuardianEmail.objects.filter(guardian = guardian, sent = True)
    if mail:
        guardian.status = "Message has already been sent."
    else:
        guardian.status = "Message Sent."
        message.send()
        models.GuardianEmail.objects.create(guardian = guardian, sent = True)
        admin_message.send()
    return render(request, 'Forms/success.html', {'guardian':guardian})


def get_a_tutor(request):
    if request.method == "POST":
        Guform = forms.GuardianForm(request.POST)
        Abform = forms.AboutChildForm(request.POST)
        Loform = forms.LocationForm(request.POST)
        Leform = forms.LessonForm(request.POST)
        if Guform.is_valid() & Abform.is_valid() & Loform.is_valid() & Leform.is_valid():
            Guf = Guform.save(commit=False)
            Guf_data = Guform.save()
            Abf = Abform.save(commit=False)
            Abf.guardian = Guf_data
            Abf_data = Abform.save()
            Lof = Loform.save(commit=False)
            Lof.guardian = Guf_data
            Lof_data = Loform.save()
            Lef = Leform.save(commit=False)
            Lef.guardian = Guf_data
            Lef_data = Leform.save()
            return redirect('succes_form', uid= Guf_data.uid )
    else:
        Guform = forms.GuardianForm()
        Abform = forms.AboutChildForm()
        Loform = forms.LocationForm()
        Leform = forms.LessonForm()

    form_context = {
        'Guform':Guform,  
        'Abform':Abform,  
        'Loform':Loform,  
        'Leform':Leform,  
    }
    return render(request, 'Forms/GetATutor.html', form_context)

@login_required
def ViewGuardians(request):
    guardian = models.Guardian.objects.all().order_by('-date_joined')
    for g in guardian:
        g.full_name = f"{g.last_name} {g.first_name}"

    return render(request, 'gaurdians.html', {'guardian':guardian})


@login_required
def ViewGuardian(request, uid):
    guardian = models.Guardian.objects.get(uid=uid)
    guardian.full_name = f"{guardian.last_name} {guardian.first_name}"
    return render(request, 'gaurdian.html', {'guardian':guardian})
