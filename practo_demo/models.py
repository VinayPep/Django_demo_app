from django.core import validators
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class user_credential(models.Model):
    credential_id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True,max_length=100)
    password = models.TextField()
    class Meta:
        verbose_name_plural = "User Credential"

class user_data(models.Model):
    user_id = models.AutoField(primary_key=True)
    email = models.OneToOneField(user_credential,on_delete = models.CASCADE)
    name = models.CharField(max_length= 50)
    role = models.CharField(max_length= 10)
    city = models.CharField(max_length= 50)
    state = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    class Meta:
        verbose_name_plural = "User Data"

class doctor_details(models.Model):
    doctor_id = models.OneToOneField(user_data,on_delete = models.CASCADE,primary_key=True)
    speciality = models.CharField(max_length=20)
    rating = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(10)])
    time_from = models.DateTimeField()
    time_to = models.DateTimeField()
    class Meta:
        verbose_name_plural = "Doctor Detail"

class appointment(models.Model):
    user_id = models.ForeignKey(user_data,db_column = 'user_id',on_delete = models.CASCADE)
    doctor_id = models.ForeignKey(doctor_details,db_column = 'doctor_id',on_delete = models.CASCADE)
    date_of_appointment = models.DateTimeField()
    time_from = models.DateTimeField()
    time_to = models.DateTimeField()
    rating = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(10)])
    status = models.BooleanField()



