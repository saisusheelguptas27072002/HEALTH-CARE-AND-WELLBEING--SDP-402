
from django.urls import path

from appointment import views
from appointment.views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'appointment'

urlpatterns = [

    path('', views.welcome, name="appointment-welcome"),
    path('home/', HomePageView.as_view(), name='home'),
    path('service', ServiceView.as_view(), name='service'),
    path('doctor/appointment/create', AppointmentCreateView.as_view(), name='doctor-appointment-create'),
    path('doctor/appointment/', AppointmentListView.as_view(), name='doctor-appointment'),
    path('<pk>/delete/', AppointmentDeleteView.as_view(), name='delete-appointment'),
    path('<pk>/patient/delete', PatientDeleteView.as_view(), name='delete-patient'),
    path('patient-take-appointment/<pk>', TakeAppointmentView.as_view(), name='take-appointment'),
    path('search/', SearchView.as_view(), name='search'),
    path('patient/', PatientListView.as_view(), name='patient-list'),
    path('aboutus/', views.aboutus, name="appointment-aboutus"),
    path('wellness/', views.wellness, name="appointment-wellness"),
    path('welcome/', views.welcome, name="appointment-welcome"),
    path('fitness/', views.fitness, name="appointment-fitness"),
    path('show/', views.show, name="appointment-show"),
    path('emp', views.emp, name="appointment-emp"),
    path('edit/<int:id>', views.edit, name="appointment-edit"),
    path('update/<int:id>', views.update, name="appointment-update"),
    path('delete/<int:id>', views.destroy, name="appointment-delete"),

    #path('patients/<int:appointment_id>', PatientPerAppointmentView.as_view(), name='patient-list'),


]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
