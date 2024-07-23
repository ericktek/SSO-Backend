from rest_framework import serializers
from .models import User, School, Student, Teacher

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'user_type']

class SchoolSerializer(serializers.ModelSerializer):
    owner = UserSerializer()

    class Meta:
        model = School
        fields = ['id', 'name', 'address', 'owner']

class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Student
        fields = ['id', 'user', 'school']

class TeacherSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Teacher
        fields = ['id', 'user', 'school']
