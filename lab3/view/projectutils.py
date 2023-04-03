from datetime import datetime
from helper import read_file
from helper import is_date
from model import Project


def Load_Projects():
    projectF = read_file('lab3/data/project.txt')
    Projects = []
    for projectline in projectF:
        projectinfo = projectline.split(":")
        project = Project(int(projectinfo[0]), projectinfo[1],
                          projectinfo[2], int(projectinfo[3]), projectinfo[4], projectinfo[5], int(projectinfo[6]))
        Projects.append(project)
    return Projects


def MenutoUpdate(project):
    choicess = '123456'
    title = details = totaltarget = startdate = enddate = ""
    while True:
        print("1- Title")
        print("2- Details")
        print("3- Start Date")
        print("4- End Date")
        print("5- Total Target")
        print("6- Cancel")
        choice = input("#>> ")
        if choice not in choicess or len(choice) > 1:
            print("In valid input")
            continue
        if choice == "1":
            while True:
                title = input("Title: ")
                if len(title) == 0 or title.isspace():
                    print("Title Can't be empty")
                    continue
                else:
                    project.title = title
                    break
        elif choice == "2":
            while True:
                details = input("Details: ")
                if len(details) == 0 or details.isspace():
                    print("Details Can't be empty")
                    continue
                else:
                    project.details = details
                    break
        elif choice == "3":
            while True:
                startdate = input(
                    "Enter Start Date in dd-mm-yy (empty is current date): ")
                if len(startdate) == 0:
                    now = datetime.now()
                    startdate = now.strftime("%d-%m-%Y")
                    break
                elif is_date(startdate, "%d-%m-%Y"):
                    project.startDate = datetime.strptime(startdate, "%d-%m-%Y").date()
                    break
                else:
                    print("Not a date Format")
                    continue
        elif choice == "4":
            while True:
                enddate = input("Enter End Date in dd-mm-yy: ")
                print(enddate)
                if len(enddate) > 0 and is_date(enddate, "%d-%m-%Y"):
                    start_date_obj = datetime.strptime(
                        str(project.startDate), "%Y-%m-%d").date()
                    end_date_obj = datetime.strptime(
                        enddate, "%d-%m-%Y").date()
                    if start_date_obj < end_date_obj:
                        print(end_date_obj)
                        project.endDate = end_date_obj
                        break
                    else:
                        print("End date must be in future after start day")
                        continue
                else:
                    print("Not a date Format")
                    continue
        elif choice == "5":
            while True:
                totaltarget = input("Target in EGP: ")
                try:
                    totaltarget = int(totaltarget)
                except ValueError:
                    print("Must be Number")
                    continue
                else:
                    project.totalTarget = totaltarget
                    break
        else:
            return
        return project

