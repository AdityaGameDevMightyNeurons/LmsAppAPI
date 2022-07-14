from django.urls import path
from lmsproj.views import Signup, SignIn,SignOut,CreateCourse,AllUsers,AllCourses,CreateBatch,AllBatch,CreateTask,AssignUser,TaskSubmit,AllTaskinfo,AllTask,ProfileDetails,GetEventsTeacherandBatchWise

urlpatterns = [
   path("Signup/",view=Signup.as_view(),name="Signup"),
   path("SignIn/",view=SignIn.as_view(),name="SignIn"),
   path("SignOut/",view=SignOut.as_view(),name="SignOut"),
   path("CreateCourse/",view=CreateCourse.as_view(),name="CreateCourse"),
   path("AllUsers/",view=AllUsers.as_view(),name="AllUsers"),
   path("AllCourses/",view=AllCourses.as_view(),name="AllCourses"),
   path("CreateBatch/",view=CreateBatch.as_view(),name="CreateBatch"),
   path("AllBatch/",view=AllBatch.as_view(),name="AllBatch"),
   path("CreateTask/",view=CreateTask.as_view(),name="CreateTask"),
   path("AssignUser/",view=AssignUser.as_view(),name="AssignUser"),
   path("TaskSubmit/",view=TaskSubmit.as_view(),name="TaskSubmit"),
   path("AllTaskinfo/",view=AllTaskinfo.as_view(),name="AllTaskinfo"),
   path("AllTask/",view=AllTask.as_view(),name="AllTask"),
   path("ProfileDetails/",view=ProfileDetails.as_view(),name="ProfileDetails"),
   path("GetEventsTeacherandBatchWise/",view=GetEventsTeacherandBatchWise.as_view(),name="GetEventsTeacherandBatchWise"),
]
