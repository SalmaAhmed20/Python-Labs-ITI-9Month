from helper import generateRandomCode
from helper import sendEmail
from helper import read_file
from email.mime.text import MIMEText
from model import User

def Load_Users():
    usersF = read_file('lab3/data/user.txt')
    users = []
    for userline in usersF:
        userinfo = userline.split(":")
        user = User(int(userinfo[0]), userinfo[1],
                    userinfo[2], userinfo[3], userinfo[4], userinfo[5])
        users.append(user)
    return users

users = Load_Users()

def check_user(email):
    for user in users:
        if user.get_email() == email:
            return True, user
    return False, None


def Verify(email):
    while True:
        verifyCode = generateRandomCode()
        message = MIMEText(f"""\
        Your Verification Code is : {verifyCode}.""")
        message['Subject'] = "Verify Crowd-Funding App "
        sendEmail(email, message.as_string())
        inVcode = input("Please Enter Verification Code: ")
        if inVcode == verifyCode:
            print("Welcome to Our system")
            return True
        else:
            print("Wrong code send another one Y(default) or (exit)? ")
            choice = input("#>>")
            if choice == "exit":
                return False
            else:
                continue

