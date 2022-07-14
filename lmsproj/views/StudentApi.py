
from rest_framework.views import APIView
from lmsproj.models import Account, Batch, Task, TaskSubmission
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from lmsproj.models import Account, TaskSubmission, Task
from lmsproj.studentserializer import TsksubmissionSerializer
from lmsproj.utils import GetCompletedandPendingTask




class TaskSubmit(APIView):
    permission_classes=[IsAuthenticated]
    def post(self, request):
        Serializer = TsksubmissionSerializer(data=request.data)
        if Serializer.is_valid(raise_exception=True):
            validated_data = request.data
            try:
                UserObj = Account.objects.get(email= request.user)
                TaskObj = Task.objects.get(id = int(validated_data["task"]))

                TaskSubmission.objects.create(student = UserObj, taskanswer = validated_data["taskanswer"],task = TaskObj )
                return Response({"msg":"Task Successfully Submited", "status":status.HTTP_201_CREATED})
            except Exception as e:
                return Response({"msg":"Task Successfully Submited","error":e, "status":status.HTTP_401_UNAUTHORIZED})

            
        else:
            return Response({"msg":"Serializer is not valid", "status":status.HTTP_417_EXPECTATION_FAILED})


class AllTaskinfo(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request):
        CurrentStudent_Id= request.user.id
        print(CurrentStudent_Id)
        Completed,Pending = GetCompletedandPendingTask(studentid=CurrentStudent_Id)
        return Response({"msg":"Student Task","data":{"completed":Completed,"pending":Pending}, "status":status.HTTP_201_CREATED})

