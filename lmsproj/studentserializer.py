from dataclasses import fields
from rest_framework import serializers
from lmsproj.models import TaskSubmission



class TsksubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskSubmission
        fields = ("taskanswer","task")
