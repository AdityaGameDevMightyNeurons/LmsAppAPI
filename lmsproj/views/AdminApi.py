from rest_framework.views import APIView
from lmsproj.models import Account, Batch, Courses, Task
from rest_framework.response import Response
from rest_framework import status


class AllUsers(APIView):
    def get(self,request):
        Data = Account.objects.all().values("id","email","password")
        return Response({"msg":"Data fetched", "data":Data, "status":status.HTTP_200_OK})


class AllCourses(APIView):
    def get(self,request):
        Data = Courses.objects.all().values("id","name","createdby","numberofmodules")
        return Response({"msg":"Data fetched", "data":Data, "status":status.HTTP_200_OK})

class AllBatch(APIView):
    def get(self,request):
        Data = Batch.objects.all().values("id","name","course","startdate","enddate")   
        return Response({"msg":"Data fetched", "data":Data, "status":status.HTTP_200_OK})

class AllTask(APIView):
    def get(self,request):
        Data = Task.objects.all().values("id","name","details","startdate","enddate","task","isActive","batch")
        return Response({"msg":"Data fetched", "data":Data, "status":status.HTTP_200_OK})

        