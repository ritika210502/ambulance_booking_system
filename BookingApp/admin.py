from django.contrib import admin
from BookingApp.models import user,hospital,ambulance,patient,hos_patient,av_hospital,av_ambulance,Emergency

# Register your models here.
admin.site.register(user)
admin.site.register(hospital)
admin.site.register(ambulance)
admin.site.register(patient)
admin.site.register(hos_patient)
admin.site.register(av_hospital)
admin.site.register(av_ambulance)
admin.site.register(Emergency)








