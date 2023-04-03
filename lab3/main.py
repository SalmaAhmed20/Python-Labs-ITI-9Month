from view import *
while True:
    print ("---We lcome to Crowd-Funding App ---")
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    choice =""
    while choice !="1" and choice !="2" and choice !="3":
        choice=input("#>> ")
        if choice !="1" and choice !="2" and choice !="3":
            print("Invalid Input")
            continue
        elif choice == "1":
            register()
        elif choice =="2":
            login()
        else:
            exit()