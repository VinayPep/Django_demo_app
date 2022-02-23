from django.db.models import fields
from rest_framework import serializers
from .models import *

class CredentialSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_credential
        fields = '__all__'

class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_data
        fields = '__all__'

class DoctorDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = doctor_details
        fields = '__all__'
class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = appointment
        fields = '__all__'
