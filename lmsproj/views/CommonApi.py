from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from lmsproj.utils import GetProfileData, GetEventsData




class ProfileDetails(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request):
        Id = request.user.id
        try:
            ObjectList = GetProfileData(userid=Id)
            print(ObjectList)
            return Response({"msg":"Profile data Scucessfully fetched","data":ObjectList, "status":status.HTTP_201_CREATED})
        except Exception as e:
            return Response({"msg":"Profile data not Scucessfully fetched","error":str(e), "status":status.HTTP_401_UNAUTHORIZED})



class GetEventsTeacherandBatchWise(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request):
        Is_Admin = request.user.is_admin
        Is_Teacher = request.user.isTeacher
        Is_Student = request.user.isStudent
        Data = GetEventsData(isAdmin=Is_Admin,isTeacher=Is_Teacher,isStudent=Is_Student,userid=request.user.id)
        return Response({"msg":"Event data Scucessfully fetched","data":Data, "status":status.HTTP_201_CREATED})

        
        

