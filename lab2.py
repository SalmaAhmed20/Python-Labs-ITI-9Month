# Problem 1
print ("#### P1 ####")
def generateArray(length:int,start:int):
    if isinstance(length,int) and isinstance(start,int):
        arr=[]
        for i in range(start,start+length):
            arr.append(i)
        return arr
    else:
        return "not valid datatype"

length=input("Enter length of the array: ")
start=input("Enter Start Point: ")
print(generateArray(int(length),int(start)))

# Problem 2
print ("#### P2 ####")
def divisibleBy3_5(num):
    if isinstance(num,int):
        if num%3==0 and num%5==0:
            return "FizzBuzz"
        elif num%3==0:
            return "Fizz"
        elif num%5==0:
            return "Buzz"
        else:
            return "Not divisible on 3 or 5"
    else:
        return "not valid datatype"
num =input("Enter the Number: ")
print(divisibleBy3_5(int(num)))

# Problem 3
print ("#### P3 ####")
def reverse():
    inpt=input("Enter your string: ")
    reverseStr= inpt[::-1]
    return reverseStr
print (reverse())

# Problem 4
import re
print ("#### P4 ####")
def has_no_numbers(name):
    return not bool(re.search(r'\d', name))
def is_valid_email(email):
    if len(email) > 7:
        if re.match(r'^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$', email) != None:
            return True
    return False
def dataValidation(name):
    if len(name) > 0 and not name.isspace() and has_no_numbers(name):
        email=input("Enter Your Email: ")
        if is_valid_email(email):
            print(f"Name: {name} \nE-mail: {email}")
        else:
            print("Not Valid Email")
    else:
        print("Wrong Name")
name=input("Enter your name: ")
dataValidation(name)

# Problem 5
print ("#### P5 ####")
def longestSubstring(inpt):
    substrArr=[]
    inpt=inpt.lower()
    substr=inpt[0]
    for i in range(0,len(inpt)-1):
        if ord(inpt[i]) < ord(inpt[i+1]):
            substr+=inpt[i+1]
        else:
            substrArr.append(substr)
            substr=inpt[i+1]
    # add final substring
    substrArr.append(substr)
    print(substrArr)
    maxlen=len(substrArr)
    maxidx=0;
    i=0;
    for substrs in substrArr:
        if maxlen < len(substrs):
            maxlen=len(substrs)
            maxidx=i
        i+=1
    return substrArr[maxidx];
print("Longest SubString is: "+longestSubstring("abdulrahman"))

# Problem 6
print ("#### P6 ####")
sum=0
while True:
    inpt=input ("Enter Number or \"done\" to exit:  ")
    if inpt.isnumeric():
        sum+=int(inpt)
    elif isinstance(inpt,str) and inpt=="done":
        break
    else:
        print(" ==Not Valid Input == ")
        continue
print(f"Total = {sum} ")

# Problem 7
import random
print ("#### P7 ####")
words=["apple","banana","orange","mango","car","bus","moon"]
randomIdx=random.randint(0,len(words)-1)
theWord=words[randomIdx]
Guessingword="_"*len(theWord)
numOfTries=7
print(theWord)
print(Guessingword)
while numOfTries > -1 and Guessingword !=theWord:
    print(f"====You have {numOfTries} tries left ====")
    print("\n======== "+Guessingword+" ========")
    inpt=input("Guess a character: ")
    if len(inpt) > 1:
        print("You Can only guess on character at time")
        continue
    positions=[]
    for i in range (len(theWord)):
        if theWord[i] == inpt :
            positions.append(i)
    if len(positions) == 0:
        print("Wrong Guess :(")
        numOfTries-=1
    else:
       for i in range (len(positions)):
            Guessingword=Guessingword[:int(positions[i])]+inpt+Guessingword[int(positions[i])+1:]
print("======== "+Guessingword+" ========")
if Guessingword == theWord:
    print("Congrats YOU WIN !!")
else:
    print("Game Over")