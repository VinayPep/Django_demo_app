from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from .serializer import *
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class RegisterAPI(APIView):
    def post(self,request):
        serializer = CredentialSerializer(data = request.data)
        #password can be hashed by hash_algo(request.data['password'])
        if not serializer.is_valid():
            return Response({'status':400,'message':'Given data is wrong'})
        else:
            serializer.save()
            return Response({'status':201,'payload':serializer.data,'message':'User is created successfully'})


class UserAPI(APIView):

    def get(self,request,pk):
        user_obj = get_object_or_404(user_data,user_id = pk)
        serializer = UserDataSerializer(user_obj)
        return Response({'status':200,'payload':serializer.data,'message':'User is fetched successfully'})
    
    def post(self,request):
    
        serializer = UserDataSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'status':400,'message':'Given data is wrong'})
        else:
            serializer.save()
            return Response({'status':201,'payload':serializer.data,'message':'User is created successfully'})
    
    def put(self,request,pk):
        try :
            user_obj = user_data.objects.get(user_id = pk)
            serializer = UserDataSerializer(user_obj,data = request.data)
            if not serializer.is_valid():
                return Response({'status':400,'message':'Given data is wrong'})
            else:
                serializer.save()
                return Response({'status':200,'payload':serializer.data,'message':'User is updated successfully'})

        except Exception as e:
            return Response({'status':404,'message':'User not found'})

    def delete(self,request,pk):
            try:
                user_objs = user_data.objects.get(user_id=pk)
                user_objs.delete()
                return Response({'status':200,'message':'Deleted Successfully'})
            except Exception as e:
                return Response({'status':403,'message':'Invalid ID'})



class DoctorAPI(APIView):

    def get(self,request,pk):
        user_obj = get_object_or_404(user_data,user_id = pk)
        doctor_obj = get_object_or_404(doctor_details,doctor_id = pk)
        serializer = UserDataSerializer(user_obj)
        doc_serializer = DoctorDetailsSerializer(doctor_obj)
        return Response({'status':200,'payload':serializer.data,'doc_payload':doc_serializer.data,'message':'User is fetched successfully'})
    
    def post(self,request):
        
        serializer = DoctorDetailsSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'status':400,'message':'Given data is wrong'})
        else:
            serializer.save()
            return Response({'status':201,'payload':serializer.data,'message':'Doctor Details is created successfully'})
    
    def put(self,request,pk):
        try :
            doc_obj = doctor_details.objects.get(doctor_id = pk)
            print(doc_obj)
            serializer = DoctorDetailsSerializer(doc_obj,data = request.data)
            if not serializer.is_valid():
                return Response({'status':400,'message':'Given data is wrong'})
            else:
                serializer.save()
                return Response({'status':200,'payload':serializer.data,'message':'User is updated successfully'})

        except Exception as e:
            return Response({'status':404,'message':'Doctor not found'})

    def delete(self,request,pk):
            try:
                doc_objs = doctor_details.objects.get(doctor_id=pk)
                doc_objs.delete()
                return Response({'status':200,'message':'Deleted Successfully'})
            except Exception as e:
                return Response({'status':403,'message':'Invalid ID'})
        
