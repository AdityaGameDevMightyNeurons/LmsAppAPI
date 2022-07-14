from rest_framework_simplejwt.tokens import RefreshToken
from lmsproj.models import Account,AssigningUser, Batch,TaskSubmission,Task
from django.contrib.auth.hashers import check_password

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

def ValidateUser(Email=None, Password = None):
    try:
        UserPass = Account.objects.filter(email = Email).values("password")[0]["password"]
        isPassCheck = check_password(Password, UserPass)
        if isPassCheck:
            Account.objects.filter(email=Email).update(is_active =True)
            UserObj = Account.objects.get(email = Email)
            return UserObj
    except:
        return None


def TeacherObjs(data):
    # print(data)
    try: 
        FirstTeacher = Account.objects.get(id = int(data["firstmoduleteacher"]))
    except:
        FirstTeacher = None

    try:
        SecondTeacher = Account.objects.get(id = int(data["secondmoduleteacher"]))
    except:
        SecondTeacher = None

    try:
        ThirdTeacher = Account.objects.get(id = int(data["thirdmoduleteacher"]))
    except:
        ThirdTeacher = None

    try:
        FourthTeacher = Account.objects.get(id = int(data["fourthmoduleteacher"]))
    except:
        FourthTeacher = None

    try:
        FifthTeacher = Account.objects.get(id = int(data["fifthmoduleteacher"]))
    except:
        FifthTeacher = None
    
    try:
        SixthTeacher = Account.objects.get(id = int(data["sixthmoduleteacher"]))
    except:
        SixthTeacher = None
    
    try:
        SeventhTeacher = Account.objects.get(id = int(data["seventhmoduleteacher"]))
    except:
        SeventhTeacher = None

    return FirstTeacher, SecondTeacher, ThirdTeacher,FourthTeacher,FifthTeacher,SixthTeacher,SeventhTeacher


def GetCompletedandPendingTask(studentid):
    
    Batch_Id = AssigningUser.objects.filter(student = 1).values("batch")[0]["batch"]
    QuarySet = Task.objects.all().filter(batch = Batch_Id).values("id","name","details","startdate","enddate","task","isActive")
    Submitted_Task_List = []
    Pending_Task_List = []

    for i in QuarySet:
        try:
            Student_id = TaskSubmission.objects.filter(task = i["id"]).values("student")[0]["student"]
            if Student_id == studentid:
                Submitted_Task_List.append(i)
        except:
            Pending_Task_List.append(i)
    

    return Submitted_Task_List, Pending_Task_List





def GetProfileData(userid):
    
    UserObj = AssigningUser.objects.select_related("batch").get(student=userid).student
    CourseObj = AssigningUser.objects.select_related("course").get(student=userid).course
    BatchObj = AssigningUser.objects.select_related("batch").get(student=userid).batch

    ObjectList = [
        {
            "name": UserObj.username,
            "email": UserObj.email,
            "phonenumber": UserObj.phonenumber,
            "datejoined": UserObj.date_joined,
            "course":CourseObj.name,
            "batch":BatchObj.name,
            "startdate": BatchObj.startdate,
            "enddate": BatchObj.enddate,
            "module": BatchObj.modulename,
        }
    ]

    return ObjectList



#Exam to be Added here in latest events
def GetEventsData(isAdmin =False,isTeacher=False,isStudent=False, userid=None):
    List = []
    List_of_Task = []

    if len(List)>0:
        List.clear()
    if len(List_of_Task)>0:
        List_of_Task.clear()

    if isAdmin:
        TaskData = Task.objects.all().values("name","startdate").order_by("-date_created")
        return TaskData
    elif isTeacher:
        obj = AssigningUser.objects.select_related("batch").filter(teacher = userid)
        
        if obj != None:
            for i in obj:
                if i.batch_id not in List:
                    List.append(i.batch_id)
                    TaskDetails = Task.objects.filter(batch = i.batch_id ).values("name","startdate").order_by("-date_created")
                    List_of_Task.append(TaskDetails)
        
            return List_of_Task

    elif isStudent:
        obj = AssigningUser.objects.select_related("batch").filter(student = userid)
        
        if obj != None:
            for i in obj:
                if i.batch_id not in List:
                    List.append(i.batch_id)
                    TaskDetails = Task.objects.filter(batch = i.batch_id ).values("name","startdate").order_by("-date_created")
                    List_of_Task.append(TaskDetails)
        
            return List_of_Task

        
                
        


            


        



