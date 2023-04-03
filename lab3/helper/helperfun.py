import re
import random
import string
from datetime import datetime

def has_no_numbers(name):
    return not bool(re.search(r'\d', name))
def is_valid_email(email):
    if len(email) > 7:
        if re.match(r'^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$', email) != None:
            return True
    return False
def is_valid_phone(phone_number):
    regex=r"^(?:\+20|0)?1[0125]\d{8}$"
    if re.match(regex,phone_number):
        return True
    return False
def generateRandomCode():
    letters = string.ascii_uppercase + string.ascii_lowercase + string.digits
    return ''.join(random.choice(letters) for i in range(5))

def is_date(string, date_format):
    try:
        datetime.strptime(string, date_format)
        return True
    except ValueError:
        return False
