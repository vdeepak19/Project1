from django.urls import path
from . import views

urlpatterns = [
    path('', views.projecthomepage, name = 'projecthomepage'),
    path('employerhomepage/', views.employerhomepage, name = 'employerhompage'),
    path('jobseekerhomepage/', views.jobseekerhomepage, name = 'jobseekerhomepage'),
    path('print/', views.print_to_console, name='print_to_console'),
    path('print1/', views.print1, name='print1'),
    path('addpagecall/',views.addpagecall,name='addpagecall'),
    path('addlogic/',views.addlogic,name='addlogic'),
    path('randompagecall/',views.randompagecall,name='randompagecall'),
    path('randomlogic/',views.randomlogic,name='randomlogic'),
    path('location_time/',views.location_time,name='location_time'),
    path('location_time_view/',views.location_time_view,name='location_time_view'),
    path('getdatepagecall/', views.getdatepagecall, name='getdatepagecall'),
    path('getdatelogic/', views.getdatelogic, name='getdatelogic'),
    path('signup/', views.signup, name = 'signup'),
    path('signup1/', views.signup1, name = 'signup1'),
    path('contactpagecall/',views.contactpagecall,name='contactpagecall'),
    path('contactlogic/',views.contactlogic,name='contactlogic'),
    path('loginpagecall/',views.loginpagecall,name='loginpagecall'),
    path('loginlogic/',views.loginlogic,name='loginlogic'),
    path('logout', views.logout, name='logout'),
    path('weatherpagecall/',views.weatherpagecall,name='weatherpagecall'),
    path('weatherlogic/',views.weatherlogic,name='weatherlogic'),
    path('send_emails/',views.send_emails,name='send_emails'),
    path('qrpagecall/',views.qrpagecall,name='qrpagecall'),
    path('qrlogic/',views.qrlogic,name='qrlogic'),
]