from helper import has_no_numbers
from helper import is_valid_email
from helper import is_valid_phone
from view.projectOp import ProjectMenu
from model import User
from helper import append_file
import time
from view.userutils import*

loginUser = ''


def login():
    email = input("E-mail: ")
    if is_valid_email(email):
        password = input("Password: ")
        isexist, user = check_user(email)
        if isexist:
            if user.get_password() == password:
                loginUser = {
                    'id': user.get_id(),
                    'First Name': user.firstName,
                    'Last Name': user.lastName,
                    'email': user.get_email()
                }
                print("Welcome IN")
                ProjectMenu(loginedUser=loginUser)
            else:
                print("Wrong Credential>>")
                return
        else:
            print("Wrong Credential>>")
            return
    else:
        print("Not Valid E-mail ")
        return


def register():
    firstName = lastName = email = password = phone = ""
    while True:
        firstName = input("First Name: ")
        if len(firstName) == 0 or firstName.isspace() or not has_no_numbers(firstName):
            print("First Name must not be Empty or contains numbers")
            continue
        else:
            break
    while True:
        lastName = input("Last Name: ")
        if len(lastName) == 0 or lastName.isspace() or not has_no_numbers(lastName):
            print("Last Name must not  be Empty or contains numbers")
            continue
        else:
            break
    while True:
        email = input("E-mail: ")
        if is_valid_email(email):
            isexist, user = check_user(email)
            if not isexist:
                break
            else:
                print("Email is Already Exist")
                continue
        else:
            print("Not Valid E-mail ")
            continue
    while True:
        password = input("Password: ")
        if len(password) > 0:
            confirmPass = input("Confirm Password: ")
            if password == confirmPass:
                break
            else:
                print("Not Match")
                continue
        else:
            print("Can't be empty ")
            continue
    while True:
        phone = input("Phone: ")
        if is_valid_phone(phone):
            break
        else:
            print("Not Valid ")
            continue
    user = User(round(time.time()), firstName,
                lastName, email, password, phone)
    if Verify(email=email):
        cont = "\n"+str(user.get_id())+":"+user.firstName+":"+user.lastName + \
            ":"+user.get_email()+":"+user.get_password()+":"+user.get_phone()
        append_file("lab3/data/user.txt", content=cont)
        users.append(user)
        print("<<You can Now Login>>")
        return
    else:
        print(" Not registered")
        return
