from rest_framework.views import APIView
from lmsproj.models import Account, Batch, Courses, Task,Exam,BatchCourseAssign
from rest_framework.response import Response
from rest_framework import status

#Must Update student and Teacher Assignment each time if it's there to be updated
class AllUsers(APIView):
    def get(self,request):
        Data = Account.objects.all().values("id","email","firstname","lastname","phonenumber","isTeacher","isStudent","password")
        print(Data)
        for i in Data:
            try:
                BatchId = BatchCourseAssign.objects.filter(user = i["id"]).values("batch")
                Course_Id = BatchCourseAssign.objects.filter(user = i["id"]).values("course")
                i["batch"] = BatchId
                i["course"] = Course_Id
            except:
                i["batch"] = "None"
                i["course"] = "None"
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

class AllExam(APIView):
    def get(self,request):
        ExamDetails = Exam.objects.all().values("name","details","examdate","duration","course",
                                                "firstquestion","firstqsnoptionone","firstqsnoptiontwo","firstqsnoptionthree","firstqsnoptionfour","firstqsnAnswer",
                                                "secondquestion","secondqsnoptionone","secondqsnoptiontwo","secondqsnoptionthree","secondqsnoptionfour","secondqsnAnswer",
                                                "thirdquestion","thirdqsnoptionone","thirdqsnoptiontwo","thirdqsnoptionthree","thirdqsnoptionfour","thirdqsnAnswer",
                                                "fourthquestion","fourthqsnoptionone","fourthqsnoptiontwo","fourthqsnoptionthree","fourthqsnoptionfour","fourthqsnAnswer",
                                                "fifthquestion","fifthqsnoptionone","fifthqsnoptiontwo","fifthqsnoptionthree","fifthqsnoptionfour","fifthqsnAnswer").order_by("-datecreated")
        return Response({"msg":"Data fetched", "data":ExamDetails, "status":status.HTTP_200_OK})


class AllAssignments(APIView):
    def get(self,request):
        AllAssignObj = BatchCourseAssign.objects.all().values("batch","course","activeModule","user")
        return Response({"msg":"Data fetched", "data":AllAssignObj, "status":status.HTTP_200_OK})


        