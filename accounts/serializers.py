from rest_framework import serializers
from django.contrib.auth.models import User
from django.core.mail import send_mail,EmailMessage
from django.conf import settings
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model=Teacher
        fields='__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model=Job
        fields='__all__'

class UserChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    confirm_new_password = serializers.CharField(required=True)

    def validate_old_password(self, value):
        user = self.context['user']
        if not user.check_password(value):
            raise serializers.ValidationError('Incorrect old password')
        return value
    def validate(self, data):
        if data['new_password'] != data['confirm_new_password']:
            raise serializers.ValidationError('New passwords do not match')
        return data

    def create(self, validated_data):
        user = self.context['user']
        user.set_password(validated_data['new_password'])
        user.save()
        return user




class SentRestEmailPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True, max_length=255)

    def validate_email(self, value):
        try:
            teacher = Teacher.objects.get(email=value)
            self.user_type = 'teacher'
            self.user = teacher.user
            self.name=teacher.name
            self.email=value
        except Teacher.DoesNotExist:
            try:
                student = Student.objects.get(email=value)
                self.user_type = 'student'
                self.user = student.user
                self.name=student.name
                self.email=value
            except Student.DoesNotExist:
                raise serializers.ValidationError('User with this email does not exist.')
        return value

    def save(self):
        new_password = User.objects.make_random_password()
        user = self.user
        user.set_password(new_password)
        user.save()
        subject = 'Reset Password'
        message = f'Hi {self.name},\n\nYour new password is: {new_password}'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [self.email]
        send_mail(subject, message, email_from, recipient_list, fail_silently=False)
        print(recipient_list)
        print(send_mail)
        print(f'New password generated for user {user.username}: {new_password}')
        print(f'Email sent to {self.email} with message:\n{message}')
        return user
    
    # def to_representation(self, instance):
    #     return {'detail': f'Password reset email sent to {self.user_type}.'}
    
                                                                         