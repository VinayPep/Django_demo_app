from django.contrib import admin
from .models import * 

# Register your models here.
admin.site.register(user_credential)
admin.site.register(user_data)
admin.site.register(doctor_details)
admin.site.register(appointment)
