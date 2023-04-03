from datetime import datetime
import time
from helper import is_date
from helper import append_file
from helper import read_file
from helper import write_file
from view.projectutils import MenutoUpdate
from view.projectutils import Load_Projects
from view.userutils import Load_Users
from model import Project


def CreateProject(user):
    id = round(time.time())
    ownerid = user['id']
    title = details = totaltarget = startdate = enddate = ""
    while True:
        title = input("Title: ")
        if len(title) == 0 or title.isspace():
            print("Title Can't be empty")
            continue
        else:
            break
    while True:
        details = input("Details: ")
        if len(details) == 0 or details.isspace():
            print("Details Can't be empty")
            continue
        else:
            break
    while True:
        totaltarget = input("Target in EGP: ")
        try:
            totaltarget = int(totaltarget)
        except ValueError:
            print("Must be Number")
            continue
        else:
            break
    while True:
        startdate = input(
            "Enter Start Date in dd-mm-yy (empty is current date): ")
        if len(startdate) == 0:
            now = datetime.now()
            startdate = now.strftime("%Y-%m-%d")
            break
        elif is_date(startdate, "%d-%m-%Y"):
            startdate=datetime.strptime(startdate,'%d-%m-%Y').date()
            break
        else:
            print("Not a date Format")
            continue
    while True:
        enddate = input("Enter End Date in dd-mm-yy: ")
        if len(enddate) > 0 and is_date(enddate, "%d-%m-%Y"):
            start_date_obj = datetime.strptime(str(startdate), "%Y-%m-%d").date()
            end_date_obj = datetime.strptime(enddate, "%d-%m-%Y").date()
            if start_date_obj < end_date_obj:
                enddate=end_date_obj
                break
            else:
                print("End date must be in future after start day")
                continue
        else:
            print("Not a date Format")
            continue
    project = Project(id, title, details, totaltarget,
                      startdate, enddate, ownerid)
    cont = str(project.id)+":"+project.title+":"+project.details + \
        ":"+str(project.totalTarget)+":"+str(project.startDate) + \
        ":"+str(project.endDate)+":"+str(project.ownerID)+"\n"
    append_file("lab3/data/project.txt", content=cont)


def ReadAllProjects():
    projects = Load_Projects()
    if len(projects) == 0:
        print("No Projects in the System")
        return
    for project in projects:
        users = Load_Users()
        name = ""
        for user in users:
            if user.get_id() == project.ownerID:
                name = user.firstName+" "+user.lastName
        print(f"P.id= {project.id},\nTitle= {project.title},\nDetails= {project.details},\nTotal Target= {project.totalTarget},\nStart Date= {project.startDate},\nEnd Date={project.endDate},\nOwner={name} ")
        print("----------------------------------------")


def UpdateProject(_id, loginedUser):
    # check for existence
    projects = Load_Projects()
    idx = 0
    if len(projects) == 0:
        print("No Projects in the System")
        return
    flag=False
    for project in projects:
        if project.id == _id:
            flag=True
            if project.ownerID == loginedUser['id']:
                while True:
                    updatedproject = project
                    updatedproject = MenutoUpdate(updatedproject)
                    print("You Want to update another field? [Y/N]")
                    choice = input("[Y/N(default)]")
                    if choice.lower() == "y":
                        continue
                    else:
                        break
            else:
                print("not your project")
                return
            break
        idx += 1
    if not flag:
        print ("No projects Founded!")
        return
    projects.pop(idx)
    projects.insert(idx, updatedproject)
    write_file('lab3/data/project.txt', "")
    for project in projects:
        cont = str(project.id)+":"+project.title+":"+project.details + \
            ":"+str(project.totalTarget)+":"+str(project.startDate) + \
            ":"+str(project.endDate)+":"+str(project.ownerID)+"\n"
        append_file("lab3/data/project.txt", content=cont)


def DeleteProject(_id, loginedUser):
    projects = Load_Projects()
    idx = 0
    if len(projects) == 0:
        print("No Projects in the System")
        return
    flag=False
    for project in projects:
        if project.id == _id:
            flag=True
            if project.ownerID == loginedUser['id']:
                break
            else:
                print("not your project")
                return
        idx += 1
    if not flag:
        print ("No projects Founded!")
        return 
    proj = projects.pop(idx)
    write_file('lab3/data/project.txt', "")
    for project in projects:
        cont = str(project.id)+":"+project.title+":"+project.details + \
            ":"+str(project.totalTarget)+":"+project.startDate + \
            ":"+project.endDate+":"+str(project.ownerID)+"\n"
        append_file("lab3/data/project.txt", content=cont)
    print("Project Deleted Successfully")


def SearchProjectByDate():
    projects = Load_Projects()
    if len(projects) == 0:
        print("No Projects in the System")
        return
    choices = '123'
    date = ''
    while True:
        print("--Search by---")
        print("1- Start Date")
        print("2- End Date")
        print("3- Exit")
        choice = input("#>>")
        if choice not in choices and len(choice) > 1:
            print("Invalid Input")
            continue
        elif choice =="1" or choice=="2":
            while True:
                date = input("Enter Date in dd-mm-yy: ")
                if is_date(date, "%d-%m-%Y"):
                    date=datetime.strptime(date,'%d-%m-%Y').date()
                    date=str(date)
                    break
                else:
                    print("Not a date Format")
                    continue
            if choice=="1":
                flag=False
                for project in projects:
                    if project.startDate==date:
                        flag=True
                        users = Load_Users()
                        name = ""
                        for user in users:
                            if user.get_id() == project.ownerID:
                                name = user.firstName+" "+user.lastName
                        print(f"P.id= {project.id},\nTitle= {project.title},\nDetails= {project.details},\nTotal Target= {project.totalTarget},\nStart Date= {project.startDate},\nEnd Date={project.endDate},\nOwner={name} ")
                        print("----------------------------------------")
                if not flag:
                    print ("No projects Founded!")
                    return
            elif choice=="2":
                flag=False
                for project in projects:
                    if project.endDate==date:
                        flag=True
                        users = Load_Users()
                        name = ""
                        for user in users:
                            if user.get_id() == project.ownerID:
                                name = user.firstName+" "+user.lastName
                        print(f"P.id= {project.id},\nTitle= {project.title},\nDetails= {project.details},\nTotal Target= {project.totalTarget},\nStart Date= {project.startDate},\nEnd Date={project.endDate},\nOwner={name} ")
                        print("----------------------------------------")
                if not flag:
                    print ("No projects Founded!")
                    return
        else:
            return
                
def ProjectMenu(loginedUser):
    menu = '123456'
    while True:
        print("1- Create a New Project ")
        print("2- Read all Project")
        print("3- Update Project")
        print("4- Delete Project")
        print("5- Search for Project by Date")
        print("6- Sign out")
        choice = input("#>> ")
        if choice not in menu and len(choice) > 1:
            print("Wrong Choice")
            continue
        else:
            if choice == "1":
                print("----------------Create a New Project-----------------")
                CreateProject(loginedUser)
            elif choice == "2":
                print("----------------Read All Projects-----------------")
                ReadAllProjects()
            elif choice == "3":
                print("----------------Update Project-----------------")
                while True:
                    try:
                        _id = int(input("Project ID: "))
                    except ValueError:
                        print("it must be number")
                        continue
                    else:
                        UpdateProject(_id, loginedUser)
                        break
            elif choice == "4":
                print("----------------Delete Project-----------------")
                while True:
                    try:
                        _id = int(input("Project ID: "))
                    except ValueError:
                        print("it must be number")
                        continue
                    else:
                        DeleteProject(_id, loginedUser)
                        break
            elif choice == "5":
                print("----------------Search By date-----------------")
                SearchProjectByDate()
            else:
                return
