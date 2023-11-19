from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.utils import timezone
from .models import Event
import base64
import os
import secrets  # For generating random nonces
import datetime



def index_view(request):
    nonce = secrets.token_urlsafe(16)
    events = Event.objects.all()  # Retrieve all Event objects
    current_year = datetime.datetime.now().year
    return render(request, 'bhlwebapp/index.html', {'events': events, 'nonce': nonce, 'current_year': current_year})

def make_appointment(request):
    if request.method == 'POST':
        print("make_appointment function called with POST request")
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        date = request.POST.get('date', '')
        department = request.POST.get('department', '')
        doctor = request.POST.get('doctor', '')
        message = request.POST.get('message', '')

        if not name or not email or not phone or not date or not department or not doctor:
            # If any required field is missing, show an error message
            messages.error(request, 'Please fill in all required fields.')
            return redirect('bhlwebapp:index')  # Redirect to the index page

        # Process the form data and perform any necessary actions
        # For example, you can send an email, save the appointment, etc.

        # Send an email with the form data
        subject = 'New Appointment Request'
        message = f'Name: {name}\nEmail: {email}\nPhone: {phone}\nDate: {date}\nDepartment: {department}\nDoctor: {doctor}\nMessage: {message}'
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = ['speaktohansnow@gmail.com']  # Replace with your email address

        try:
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)
        except Exception as e:
            # If there's an error sending the email, show an error message
            messages.error(request, 'An error occurred while processing your request. Please try again later.')
            return redirect('bhlwebapp:index')  # Redirect to the index page

        messages.success(request, 'Your appointment request has been received. We will get back to you as soon as possible.')
        appointment_success = 'Your appointment request has been received. We will get back to you as soon as possible.'
        print("Appointment processed successfully")
        return render(request, 'bhlwebapp/index.html', {'appointment_success': appointment_success, 'bochi_form_success': 'bochi-form'})
    else:
        # Render the appointment form template for GET requests
        return render(request, 'bhlwebapp/index.html')


def contact_us(request):
    contact_success = None  # Initialize the contact success message
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')

        if not name or not email or not subject or not message:
            # If any required field is missing, show an error message
            messages.error(request, 'Please fill in all required fields.')
            return redirect('bhlwebapp:index')  # Redirect to the index page

        # Process the form data and perform any necessary actions
        # For example, you can send an email, save the contact, etc.

        # Send an email with the form data
        message = f'Name: {name}\nEmail: {email}\nSubject: {subject}\nMessage: {message}'
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = ['speaktohansnow@gmail.com']  # Replace with your email address

        try:
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)
        except Exception as e:
            # If there's an error sending the email, show an error message
            messages.error(request, 'An error occurred while processing your request. Please try again later.')
            return redirect('bhlwebapp:index')  # Redirect to the index page

        messages.success(request, 'Your message has been received. We will get back to you as soon as possible. Thank you!.')
        contact_success = 'Your message has been received. We will get back to you as soon as possible. Thank you!'
        print("Contact processed successfully")
        return render(request, 'bhlwebapp/index.html', {'contact_success': contact_success, 'contact_form_success': 'contact-form'})
    else:
        # Render the appointment form template for GET requests
        return render(request, 'bhlwebapp/index.html')



def custom_404(request, exception):
        return render(request, 'bhlwebapp/404.html', status=404)