# problem1
print("#########-P1-###########")
vowels='aeiou'
count=0
inpt=input("Enter your input ")
for ch in inpt :
    if ch.lower() in vowels:
        count+=1
temp = f"Number of Vowels in \" {inpt}\" = {count} "
print(temp)

# problem 2
print("#########-P2-###########")
i=0
rng=range(0,5)
arr=[]
for i in rng:
    inpt=input("Enter element #"+str((i+1))+" ")
    arr.append(inpt)
print(f"Before sorting: {arr}" )
arr.sort()
print(f"Sorted Ascending: {arr}")
arr.sort(reverse=1)
print(f"Sorted Descending: {arr}")

#proplem 3
print("#########-P3-###########")
inpt=input("Enter your string ")
print("Number of Occurrence of \"iti\"= "+str(inpt.count('iti')))

# problem 4
print("#########-P4-###########")
vowels='aeiouAEIOU'
result=''
inpt=input("Enter your word ")
for ch in inpt:
    if ch not in vowels:
        result+=ch
numOfVowels=len(inpt)-len(result)
print(f"Number of vowels removed {numOfVowels}")
print(f"Word without vowels {result}")

# problem 5 
print("#########-P5-###########")
positions=[]
inpt=input("Enter your string ")
for i in range (len(inpt)):
    if inpt[i] == "i" :
        positions.append(i)
print(positions)
# problem 6
print("#########-P6-###########")
inpt=""
while(not inpt.isdigit()):
    inpt=input("Enter a number ")
num=int(inpt)
multiTable=[]
for i in range(1,num+1) :
    entity=[]
    for j in range(1,i+1):
        entity.append(i*j)
    multiTable.append(entity)
print(multiTable)

#problem 7
print("#########-P7-###########")
inpt=""
while(not inpt.isdigit()):
    inpt=input("Enter a number ")
num=int(inpt)
for i in range(1,num+1):
    print(" "*(num-i)+"*"*i)



