from django.shortcuts import render,redirect
def projecthomepage(request):
    return render(request,'adminapp/projecthomepage.html')

from django.contrib.auth.decorators import login_required
@login_required(login_url='loginpagecall')
def employerhomepage(request):
    return render(request, 'employerapp/employerhomepage.html')
@login_required(login_url='loginpagecall')
def jobseekerhomepage(request):
    return render(request, 'jobseekerapp/jobseekerhomepage.html')

def print1(request):
    return render(request, 'adminapp/print_to_console.html')

def print_to_console(request):
    if request.method == "POST":
        user_input = request.POST['user_input']
        print(f'User input: {user_input}')
    # return HttpResponse('Form submitted successfully')
    a1= {'user_input':user_input}
    return render(request,'adminapp/print_to_console.html',a1)

def addpagecall(request):
    return render(request, 'adminapp/addexample.html')
def addlogic(request):
    if request.method == "POST":
        number1 = int(request.POST['number1'])
        number2 = int(request.POST['number2'])
        number3 = number1 + number2
    a1= {'number3':number3}
    return render(request,'adminapp/addexample.html',a1)

import random
import string
def randompagecall(request):
    return render(request, 'adminapp/randomexample.html')
def randomlogic(request):
    if request.method == "POST":
        number1 = int(request.POST['number1'])
        ran = ''.join(random.sample(string.ascii_uppercase + string.digits, k=number1))
    a1 = {'ran':ran}
    return render(request,'adminapp/randomexample.html',a1)

from .forms import LocationForm
from datetime import datetime
import pytz
def location_time(request):
    return render(request,'adminapp/location_time.html')

def location_time_view(request):
    current_time = None
    selected_location = None
    if request.method == 'POST':
        form = LocationForm(request.POST)  # Bind the form with POST data
        if form.is_valid():
            selected_location = form.cleaned_data['timezone']
            timezone = pytz.timezone(selected_location)
            current_time = datetime.now(timezone)
            print(f"Selected Location: {selected_location}")
            print(f"Current Time: {current_time}")
    else:
        form = LocationForm()  # If GET request or initial form display

    context = {
        'form': form,
        'current_time': current_time.strftime('%Y-%m-%d %H:%M:%S') if current_time else None,
        'selected_location': selected_location,
    }
    print("Context Data:", context)
    return render(request, 'adminapp/location_time.html', context)

from .forms import *
from datetime import timedelta
from datetime import datetime
def getdatepagecall(request):
    return render(request,'adminapp/get_date.html')

def getdatelogic(request):
    if request.method == 'POST':
        form = IntegerDateForm(request.POST)
        if form.is_valid():
            integer_value = form.cleaned_data['integer_value']
            date_value = form.cleaned_data['date_value']
            updated_date = date_value + timedelta(days=integer_value)

            return render(request, 'adminapp/get_date.html', {'updated_date': updated_date})
        else:
            form = IntegerDateForm()
        return render(request, 'adminapp/get_date.html', {'form': form})

def signup(request):
    return render(request, 'adminapp/signup.html')

from django.contrib import messages
from django.contrib.auth.models import User,auth
def signup1(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['password']
        pass2 = request.POST['password1']
        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'OOPS! Username already taken.')
                return render(request, 'adminapp/signup.html')
            else:
                user = User.objects.create_user(username=username, password=pass1)
                user.save()
                messages.info(request, 'Account created Successfully!')
                return render(request, 'adminapp/Projecthomepage.html')
        else:
            messages.info(request, 'Password does not match.')
            return render(request, 'adminapp/signup.html')

from django.http import HttpResponse
from .models import *
def contactpagecall(request):
    return render(request, 'adminapp/contact.html')
def contactlogic(request):
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        comment = request.POST['comment']
        data = contactus(firstname=firstname, lastname=lastname, email=email, comments=comment)
        data.save()
        subject = 'Thank You for ur valuable Feedback'
        send_mail(
            subject,
            comment,
            'randomloginat@gmail.com',  # Update with your sender email
            [email],
            fail_silently=False,
        )
        return HttpResponse("<h1><center>Thank you giving Feedback </center></h1>")
    else:
        HttpResponse("<h1>error</h1>")


def loginpagecall(request):
    return render(request, 'adminapp/login.html')
def loginlogic(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['password']
        user = auth.authenticate(username=username, password=pass1)
        if user is not None:
            auth.login(request, user)
            if len(username)==10:
                return redirect('jobseekerhomepage')
            elif len(username)==4:
                return redirect('employerhompage')
            else:
                return redirect('projecthomepage')
        else:
            messages.info(request, 'Invalid Credentials')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('projecthomepage')

import requests
def weatherpagecall(request):
    return render(request, 'adminapp/weatherappinput.html')

def weatherlogic(request):
    if request.method == 'POST':
        place = request.POST['place']
        API_KEY = '98c9fe0696484df631f05ef073b66aa4'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={place}&appid={API_KEY}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            temperature1= round(temperature - 273.15,2)
            return render(request, 'adminapp/weatherappinput.html',
                          {'city': str.upper(place), 'temperature1': temperature1, 'humidity': humidity})
        else:
            error_message = 'City not found. Please try again.'
            return render(request, 'adminapp/weatherappinput.html', {'error_message': error_message})

import csv
from django.core.mail import send_mail
def send_emails(request):
    csv_file_path = r'D:\Personal\KL University\PFSD Workspace\PFSD Workspace\Django Projects\KLJobportal\static\mailfile.csv'
    with open(csv_file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            recipient_email = row['email']
            subject = 'Hello KLUian'  # Set your subject here
            message_body = 'Hey, Welcome to PFSD Class, Hope u have a great time with python'  # Set your email content here
            send_mail(
                subject,
                message_body,
                'randomloginat@gmail.com',  # Update with your sender email
                [recipient_email],
                fail_silently=False,
            )
            print(f'Sent email to {recipient_email}')
    return render(request, 'adminapp/Emails_sent_successfully.html')

def qrpagecall(request):
    return render(request, 'adminapp/qrpagecall.html')
import qrcode
from django.conf import settings
import os
def qrlogic(request):
    if request.method == "POST":
        user_input = request.POST['user_input']
        print(f'User input: {user_input}')
        data = user_input
        qr = qrcode.QRCode(version=1, box_size=20, border=5)
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color='black', back_color='white')

    # Save the QR code image to the static directory
        img_path = os.path.join(settings.STATICFILES_DIRS[0], 'KLU1.png')
        img.save(img_path)

    return render(request, 'adminapp/qrpagecall.html', {'img_path': 'KLU1.png'})
