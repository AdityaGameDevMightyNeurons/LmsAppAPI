from pyexpat import model
from rest_framework import serializers
from lmsproj.models import Courses, Exam, Task, Batch




class CreateCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = ("name","details","numberofmodules",
                "fistmodulename","fistmoduledays","firstmoduleteacher",
                "secondmodulename","secondmoduledays","secondmoduleteacher",
                "thirdmodulename","thirdmoduledays","thirdmoduleteacher",
                "fourthmodulename","fourthmoduledays","fourthmoduleteacher",
                "fifthmodulename","fifthmoduledays","fifthmoduleteacher",
                "sixthmodulename","sixthmoduledays","sixthmoduleteacher",
                "seventhmodulename","seventhmoduledays","seventhmoduleteacher")



class CreateBatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batch
        fields = ("name","details","startdate",
                "enddate","course","modulename",
                "isActive")

class CreateTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ("name","details","startdate",
                "enddate","batch","task")
