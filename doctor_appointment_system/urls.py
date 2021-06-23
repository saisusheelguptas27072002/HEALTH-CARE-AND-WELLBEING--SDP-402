"""
doctor_appointment_system URL Configuration

"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from appointment.views import PatientListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('', include('appointment.urls')),
    path('', include('store.urls')),
    #path('', include('calorie.urls')),
    path('', include('django.contrib.auth.urls')),



]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
