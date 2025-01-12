from .models import Assignment
from rest_framework import serializers


class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = ['title','obtain_marks','total_marks','course' ]
    
