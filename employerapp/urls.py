from django.urls import path
from . import views

urlpatterns = [
    path('addnewjobpost/', views.addnewjobpost, name = 'addnewjobpost'),
    path('add_job_details/', views.add_job_details, name = 'add_job_details'),
    path('view_job_details/', views.view_job_details, name = 'view_job_details'),
    path('delete/<int:job_id>/',views.delete_job_details,name='delete_job_details'),
    path('edit/<int:job_id>/', views.edit_job_details, name='edit_job_details'),
    path('view/', views.view_job_details, name='view_job_details'),
    path('job_application_list/',views.job_application_list,name='job_application_list'),
    path('schedule-interview/', views.schedule_interview, name='schedule_interview'),
]
