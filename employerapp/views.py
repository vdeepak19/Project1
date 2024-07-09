from django.shortcuts import render,redirect, get_object_or_404
from .models import *

# Create your views here.
from django.contrib.auth.decorators import login_required
@login_required(login_url='loginpagecall')
def addnewjobpost(request):
    return render(request,'employerapp/addnewjobpost.html')

def add_job_details(request):
    if request.method == 'POST':
        work_title = request.POST.get('workTitle')
        salary_offered = request.POST.get('salaryOffered')
        job_type = request.POST.get('jobType')
        benefits = request.POST.get('benefits')
        education = request.POST.get('education')
        work_location = request.POST.get('workLocation')
        required_skills = request.POST.get('requiredSkills')

        job_details = JobDetails(
            work_title=work_title,
            salary_offered=salary_offered,
            job_type=job_type,
            benefits=benefits,
            education=education,
            work_location=work_location,
            required_skills=required_skills,
        )
        job_details.save()
        return render(request, 'employerapp/employerhomepage.html')
    return render(request, 'employerapp/employerhomepage.html')

from django.contrib.auth.decorators import login_required
@login_required(login_url='loginpagecall')
def view_job_details(request):
    job_details_list = JobDetails.objects.all()
    return render(request, 'employerapp/view_job_details.html', {'job_details_list':job_details_list})


def delete_job_details(request, job_id):
    job_details = get_object_or_404(JobDetails, id=job_id)
    if request.method == 'POST':
        job_details.delete()
        return redirect('view_job_details')
    return render(request, 'employerapp/delete_job_details.html', {'job_details': job_details})

def edit_job_details(request, job_id):
    job_details = get_object_or_404(JobDetails, id=job_id)
    if request.method == 'POST':
        job_details.work_title = request.POST.get('workTitle')
        job_details.salary_offered = request.POST.get('salaryOffered')
        job_details.job_type = request.POST.get('jobType')
        job_details.benefits = request.POST.get('benefits')
        job_details.education = request.POST.get('education')
        job_details.work_location = request.POST.get('workLocation')
        job_details.required_skills = request.POST.get('requiredSkills')
        job_details.save()
        return redirect('view_job_details')
    return render(request, 'employerapp/edit_job_details.html', {'job_details':job_details})

from jobseekerapp.models import JobApplication
def job_application_list(request):
    job_applications = JobApplication.objects.all()
    return render(request, 'employerapp/job_application_list.html', {'job_applications':job_applications})


# views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.conf import settings
import json

@csrf_exempt
def schedule_interview(request):
    if request.method == "POST":
        data = json.loads(request.body)
        email = data.get('email')
        date = data.get('date')

        if not email or not date:
            return JsonResponse({"success": False, "error": "Missing email or date."})

        # Send email
        subject = 'Interview Scheduled'
        message = f'Congratulations Aspirant, You have been Shortlisted and Your interview is scheduled on {date}. Be report to the HR Office by 9.00am on the specified date along with all the educational documents'
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [email]

        try:
            send_mail(subject, message, from_email, recipient_list)
            return JsonResponse({"success": True})
        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)})

    return JsonResponse({"success": False, "error": "Invalid request method."})
