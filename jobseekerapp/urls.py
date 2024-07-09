from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('job_details_list', views.job_details_list, name='job_details_list'),
    path('apply/<int:job_id>/', views.apply_to_job, name='apply_to_job'),
    path('jobs/search/', views.job_search, name='job_search'),
    path('submit_form/',views.submit_form,name='submit_form'),
    path('addjobseekerprofile/',views.addjobseekerprofile,name='addjobseekerprofile'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

