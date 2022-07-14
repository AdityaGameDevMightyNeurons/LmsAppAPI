from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from lmsproj.assiginingserializer import AssigningUserSerializer
from lmsproj.models import Account, Batch, Courses,AssigningUser


class AssignUser(APIView):
    permission_classes=[IsAuthenticated]
    def post(self,request):
        Serializer = AssigningUserSerializer(data=request.data)
        if Serializer.is_valid(raise_exception=True):
            validated_data = request.data
            print(validated_data)
            try:
                BatchObj = Batch.objects.get(id = int(validated_data["batch"]))
                CourseObj = Courses.objects.get(id = int(validated_data["course"]))
                StudentObj = Account.objects.get(id = int(validated_data["student"]))
                TeacherObj = Account.objects.get(id = int(validated_data["teacher"]))

                AssigningUser.objects.create(batch = BatchObj,course = CourseObj,activeModule= validated_data["activeModule"],student = StudentObj,teacher = TeacherObj)
                return Response({"msg":"Course Batch and Module is Assigned", "status":status.HTTP_201_CREATED})
            except Exception as e:
                return Response({"msg":"Course Batch and Module is not Assigned","error":e, "status":status.HTTP_417_EXPECTATION_FAILED})

        return Response({"msg":"Course Batch and Module is not Assigned","error":"Serializer is not Valid", "status":status.HTTP_401_UNAUTHORIZED})
