class User:
    def __init__(self,ID,firstName,lastName,email,password,phone):
        self.__id=ID
        self.firstName=firstName
        self.lastName=lastName
        self.__email=email #private variable
        self.__password=password #private variable
        self.__phone=phone
        #activate function call
    def __str__(self) -> str:
        return f"User({vars(self)})"
    def get_id(self):
        return self.__id
    def get_email(self):
        return self.__email
    def get_password(self):
        return self.__password
    def get_phone(self):
        return self.__phone