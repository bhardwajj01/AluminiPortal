from django.shortcuts import render
from .models import *
from rest_framework.response import Response
from .serializers import *
from .paginations import CustomPagination
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet,ViewSet
from django.contrib.auth.models import User
from django.contrib.auth import logout
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.permissions import AllowAny,IsAdminUser,IsAuthenticated
from rest_framework import authentication, permissions, status
from rest_framework_simplejwt.authentication import JWTAuthentication  
from rest_framework.response import Response
from django.core.mail import send_mail,EmailMessage
import base64
from django.conf import settings
from rest_framework.exceptions import PermissionDenied
from rest_framework.pagination import PageNumberPagination



class LoginViewSet(ViewSet):
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]
    def create(self, request):
        username=request.data.get('username')
        password=request.data.get('password')
        # username,password = (base64.b64decode(username).decode("ascii"), base64.b64decode(password).decode("ascii"))
 
        # username= base64.b64decode(username).decode("ascii") #'utf-8'
        # password= base64.b64decode(password).decode("ascii") #'utf-8'
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            data={
                "status": False,
                "message": "User does not exist"
            } 
            return Response(data)

        if user.is_superuser:
            user_type = 'admin'
        elif Teacher.objects.filter(user=user).exists():
            user_type = 'teacher'
        elif Student.objects.filter(user=user).exists():
            user_type = 'student'
        else:
            user_type = 'unknown'

        if not user.check_password(password):
            data={
                "status": False,
                "message": "Invalid password"
            }
            return Response(data)

        token=AccessToken.for_user(user)
        token=str(token)

        return Response({
            'status': True,
            'message': 'Login successful',
            'token': token,
            'user_type': user_type
        })


class UserChangepasswordViewSet(ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def create(self, request):
        serializer=UserChangePasswordSerializer(data=request.data,context={'user':request.user})
        if serializer.is_valid(raise_exception=True):
            data={
                "status":True,
                "message": "Password Changed Successfully"
            }
            return Response(data)
        else:
            data={
                "status":False,
                "message": "Password Change Failed"
            }
            return Response(data)


class ResetPasswordEmailViewSet(ViewSet):
    permission_classes = []
    authentication_classes = []
    serializer_class = SentRestEmailPasswordSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            data={
                "status":True,
                "message": "Password Reset Email Sent Successfully"
            }
            return Response(data)
        else:
            data={
                "status":False,
                "message": "Password Reset Email Failed"
            }
        return Response(data)


class TeacherViewSet(ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]                                                                                               
    def create(self,request):
        user_id=request.user.id
        print(user_id)
        try:
            user = User.objects.get(id=user_id) 
        except Exception as e:
            print(e)
            return Response({"status":False,"message":"User not found!"})
        
        username=request.data.get('username')
        password=request.data.get('password') 
        data={
                'username':username,
                'password':password,
            }
        user=User.objects.filter(username=username).exists()
        
        if user:
            print("user already exist"),
            data={
                    'status':False,
                    'message':'User already exist'
                }
            return Response(data)
        else:
            # print("user alredy exits")
            user=User.objects.create_user(**data) 
            user.save()
            print(user)
            try:

                teacher=Teacher.objects.create(
                    user=user,
                    name=request.data.get('name'),
                    role=request.data.get('role'),
                    email=request.data.get('email'))
                teacher.save()
                print(teacher)
                
                subject = 'Welcome to MySite!'
                message = f'Hi \n this is your username: {user.username}, \n and your password is: {password}'
                # Set the email sender and recipient
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [teacher.email,]
                # Send the email using Django's email sending library
                send_mail(subject, message, email_from, recipient_list, fail_silently=False)
                print(send_mail)
                data={
                    'status':True,
                    'message':'Teacher created successfully'
                }
                return Response(data)
            except Exception as e:
                print(e)
                data={
                    'status':False,
                    'message':'Failed to create Teacher',
                    'error':str(e)

                }
                return Response(data)

    def list(self, request):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        data = {
            'data': serializer.data,
            'status': True,
        }
        return Response(data)


class StudentViewSet(ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    

    
    def create(self,request):
        user_id=request.user.id
        print(user_id)
        
        try:
            teacherObj = Teacher.objects.get(user=user_id)

        except Exception as e:
            print(e)
            return Response({"status":False,"message":"Teacher not found!"})

        print(user_id)
        username=request.data.get('username')
        password=request.data.get('password')
        data={
                'username':username,
                'password':password,
            }
        user=User.objects.filter(username=username).exists()
        
        if user:
            print("user already exist"),
            data={
                    'status':False,
                    'message':'User already exist'
                }
            return Response(data)
        else:
            # print("user alredy exits")
            user=User.objects.create_user(**data) 
            user.save()
            # print(user)

            try:
                student =Student.objects.create(
                    user=user,
                    teacher=teacherObj,
                    registeration_no=request.data.get('registeration_no'),
                    name=request.data.get('name'),
                    email=request.data.get('email'))
                student.save()
                subject = 'Welcome to MySite!'
                message = f'Hi \nthis is your username: {user.username}, \nand your password is: {password}'
                # Set the email sender and recipient
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [student.email,]
                # Send the email using Django's email sending library
                send_mail(subject, message, email_from, recipient_list, fail_silently=False)
                print(send_mail)
                data={
                    'status':True,
                    'message':'Student created successfully'
                }
                print("Student created successfully")
                return Response(data)
            except Exception as e:
            
                data={
                    'status':False,
                    'message':'Failed to create Student',
                    'error':str(e)
                }
                print("Failed to create Student")
                return Response(data)  
            
    def list(self, request):
        user_id=request.user.id
        if Teacher.objects.filter(user=user_id):
            students = Student.objects.all()
            serializer = StudentSerializer(students, many=True)
            data = {
                'status': True,
                'data': serializer.data,                
             }
            return Response(data)
        else:
            data={
                'status':False,
                'message':'You are not authorized to access this resource'
            }
            return Response(data)
            

   
class ProfileUpdateViewSet(ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def retrieve(self, request,pk=1):
        try:
            teacherdata = Teacher.objects.get(user=request.user)
            serializer = TeacherSerializer(teacherdata,context={"request":request})
            data = {
                'status': True,
                'data': serializer.data,
                }
            return Response(data)
        except Teacher.DoesNotExist:
            try:
                studentdata = Student.objects.get(user=request.user)
                serializer = StudentSerializer(studentdata,context={"request":request})
                data = {
                    'status': True,
                    'data': serializer.data,
                    }
                return Response(data)
            except Student.DoesNotExist:
                data={
                    'status':False,
                    'message':'User is not logged in'
                    }
                return Response(data)

    def update(self, request,pk=1):
        try:
            teacherdata = Teacher.objects.get(user=request.user)
            serialzedData = TeacherSerializer(instance=teacherdata, data=request.data, partial=True)
            serialzedData.is_valid(raise_exception=True)
            serialzedData.save()
            data = {
                'status': True,
                'data': serialzedData.data,
                }
            return Response(data)
        except Teacher.DoesNotExist:
            try:
                studentdata = Student.objects.get(user=request.user)
                serialzedData = StudentSerializer(instance=studentdata, data=request.data, partial=True)
                serialzedData.is_valid(raise_exception=True)
                serialzedData.save()
                data = {
                    'status': True,
                    'data': serialzedData.data,
                    }
                return Response(data)
            except Student.DoesNotExist:
                data={
                    'status':False,
                    'message':'User is not logged in'
                }
                return Response(data)

    def partial_update(self, request,pk=1):
        try:
            teacherdata = Teacher.objects.get(user=request.user)
            serialzedData = TeacherSerializer(instance=teacherdata, data=request.data, partial=True)
            serialzedData.is_valid(raise_exception=True)
            serialzedData.save()
            data = {
                'status': True,
                'data': serialzedData.data,
                }
            return Response(data)
        except Teacher.DoesNotExist:
            try:
                studentdata = Student.objects.get(user=request.user)
                serialzedData = StudentSerializer(instance=studentdata, data=request.data, partial=True)
                serialzedData.is_valid(raise_exception=True)
                serialzedData.save()
                data = {
                    'status': True,
                    'data': serialzedData.data,
                    }
                return Response(data)
            except Student.DoesNotExist:
                data={
                    'status':False,
                    'message':'User is not logged in'
                    }
                return Response(data)

class SearchViewSet(ViewSet): 
    authentication_classes = []
    permission_classes = []
    serializer_class=StudentSerializer
    queryset=Student.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields=['name']

    def list(self, request):
        name = self.request.query_params.get('name')
        queryset = Student.objects.filter(name=name)
        serializer=self.serializer_class(queryset,many=True)
        return Response(serializer.data)
        # name=request.data.get("name")
        # student_name=Student.objects.filter(name=name)
        # serializer=self.serializer_class(student_name,many=True)
        # return Response(serializer.data,status=status.HTTP_200_OK)

 

class CreateJobViewSet(ModelViewSet):
    authentication_classes = []
    permission_classes = []
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [permissions.IsAuthenticated]
    queryset = Job.objects.all()
    pagination_class = CustomPagination
    serializer_class = JobSerializer
    queryset = Job.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description', 'company', 'location']
    
    def list(self, request, *args, **kwargs):
        queryset=Job.objects.all() 
        queryset=self.paginate_queryset(queryset)
        queryset=self.filter_queryset(queryset)
        serializers=JobSerializer(queryset,many=True,context={"request":request})
        data=serializers.data
        data={
            'status':True,
            'data':data,
        }
        return Response(data)
    
    def create(self, request):
        data=request.data.copy()
        new_data={}
        for key,value in data.items():
            new_data[key]=value
 
        user_id=request.user.id
        data['created_by']=user_id
        print(data)

        serializer=JobSerializer(data=data)
        print(serializer)

        if serializer.is_valid():
            serializer.save()
            data = {
                'status': True,
                'data': serializer.data,
                'created_by': request.user.username,
                'message': 'Job created successfully'
            }
            return Response(data)
        else:
            data = {
                'status': False,
                'message': 'Job not created',
            }
            return Response(data)


class GalleryViewSet(ModelViewSet):
    authentication_classes = []
    permission_classes = []
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer

class EventViewSet(ModelViewSet):
    
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = CustomPagination

    queryset = Event.objects.all()
    serializer_class = EventSerializer
    def create(self, request):
        data = request.data.copy()
        try:
            teacher = Teacher.objects.get(user_id=request.user.id)
            data['created_by'] = teacher.id
            serializer = EventSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                data = {
                    'status': True,
                    'data': serializer.data,
                    'created_by': teacher.user.username,
                    'message': 'Event created successfully'
                }
                return Response(data)
            else:
                data = {
                    'status': False,
                    'message': 'Invalid data',
                    'errors': serializer.errors
                }
                return Response(data)
        except Teacher.DoesNotExist:
            data = {
                'status': False,
                'message': 'Teacher not found',
            }
            return Response(data)    

        
class ChatViewSet(ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request):
        sender = request.query_params.get('sender')
        receiver = request.query_params.get('receiver')   
        queryset = self.filter_queryset(self.get_queryset())

        if sender is not None and receiver is not None:
            if str(request.user.id) != receiver:
                raise PermissionDenied("You are not allowed to access these messages.")

            messages = queryset.filter(sender_id=sender, receiver_id=receiver, is_read=False)
            for message in messages:
                message.is_read = True
                message.save()
            serializer = self.get_serializer(messages, many=True)
        else:
            serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)

   
# class LogoutViewSet(ViewSet):
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [IsAuthenticated]
#     def create(self, request):
#         token = AccessToken.for_user(user=request.user)
#         token.delete()
#         return Response({
#             'status': True,
#             'message': 'Successfully logged out'
#             })


       
