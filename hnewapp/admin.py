from django.contrib import admin

from hnewapp.models import Doctor, Patient, Appoinment

# Register your models here.
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Appoinment)