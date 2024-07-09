from django.shortcuts import render

# Create your views here.


from employerapp.models import JobDetails


def job_details_list(request):
    job_details_list = JobDetails.objects.all()
    return render(request, 'jobseekerapp/viewjobs.html', {'job_details_list': job_details_list})


from django.shortcuts import render, redirect, get_list_or_404,get_object_or_404
from django.http import HttpResponse
from django.core.mail import send_mail
from .forms import *
def apply_to_job(request,job_id):
    job_details = get_object_or_404(JobDetails, id=job_id)
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            job_application = form.save(commit=False)
            job_application.job_details = job_details
            job_application.save()

            subject = 'Job Application Received'
            message = 'Thank you for applying to the Job. Your application is received and will be sent to next process'
            from_email = 'randomloginat@gmail.com'
            recipient_list = [job_application.email]
            send_mail(subject, message, from_email, recipient_list)
        return redirect('job_details_list')
    else:
        form = JobApplicationForm()

    return render(request, 'jobseekerapp/apply_to_job.html', {'job_details': job_details, 'form': form})


def job_search(request):
    query = request.GET.get('q')
    if query:
        job_details_list = JobDetails.objects.filter(work_title__icontains=query)
    else:
        job_details_list = JobDetails.objects.all()

    context = {'job_details_list': job_details_list}
    return render(request, 'jobseekerapp/viewjobs.html', context)

def addjobseekerprofile(request):
    return render(request, 'jobseekerapp/addjobseekerprofile.html')

def submit_form(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone_number = request.POST['phone_number']
        address = request.POST['address']
        tenth_marks = request.POST['10thMarks']
        twelfth_marks = request.POST['12thMarks']
        cgpa = request.POST['cgpa']
        expected_salary = request.POST['expectedSalary']
        position = request.POST['position']

        applicant = Applicant(first_name=first_name,
                              last_name=last_name,
                              phone_number=phone_number,
                              address=address,
                              tenth_marks=tenth_marks,
                              twelfth_marks=twelfth_marks,
                              cgpa=cgpa,
                              expected_salary=expected_salary,
                              position=position)
        applicant.save()
        return render(request, 'jobseekerapp/jobseekerhomepage.html')
    return render(request, 'jobseekerapp/jobseekerhomepage.html')
