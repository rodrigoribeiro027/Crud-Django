from rest_framework import serializers
from EmployeeApp.models import Departments,Employess

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Departments 
        fields=('DepartmentId','DepartmentName')

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employess
        fields=('EmployeeId','EmployeeName','Department','DateOfJoining','PhotoFileName')