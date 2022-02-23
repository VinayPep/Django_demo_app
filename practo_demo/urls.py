from django.urls import path
from . import views

urlpatterns = [
    path('user',views.UserAPI.as_view()),
    path('user/<int:pk>',views.UserAPI.as_view()),
    path('doctor/',views.DoctorAPI.as_view()),
    path('doctor/<int:pk>',views.DoctorAPI.as_view())
    

]