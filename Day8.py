from collections import Counter

#1) Write a Python script to merge two Python dictionaries

dict1={1:'a',2:'b',3:'c',4:'d'}
dict2={5:'x',6:'y',7:'z'}
dict1.update(dict2)
print(dict1)


print()
#2)Write a program to sort the value from descending to ascending in list and convert it in to a set

li=[8,6,2,5,4,1,4,9,1,4,3]
li.sort()
print("ascending list:") 
print(li)

print()
print("descending list:") 
li.sort(reverse=True)
print(li)

print()
print("set:")
s=set(li) 
print(s) 


print()
#3) Write a Python program to list number of items in a dictionary key and sort the list with the help of a function & without the function.
dict1={'a':[12,13,21,16],'b':[12,67,54,43],'c':[34,87,88,98],'d':[33,66,55,44]}
result={k:sorted(dict1[k]) for k in sorted(dict1)}
print(result)

def function1(dict1):
    res = dict()
    for key in sorted(dict1):
        res[key] = sorted(dict1[key])
    return res

function1(dict1)

 
def function2(dict1):
    res=dict()
    min1=dict1[key]
    for key in sorted(dict1):
        if dict1[key]<min1:
            min1=dict1[key]
            res[key]=min1
    return res

function1(dict1)

print()
#4)Write a Python program to get a string from a given string (user input) and change the first occurrence of the word to a user specified input.

def fun1():
    user=input("Enter the string :")
    word="String is given by user  "
    return word.replace('String',user)
fun1()

print()
#5)Write a Python program to get a string from a given string where all occurrences of its first char have been changed to capital letter.

def f3():
    user=input("Enter the string :")
    return user.capitalize()
f3()
print()
#6) Write a Python program to find the repeated items of a list

 
l1 = [1,2,1,2,3,4,5,1,1,2,5,6,7,8,9,9]
d = Counter(l1)
print(d)
 
new_list = list([item for item in d if d[item]>1])
print(new_list)
print()
#7) Write a Python program to check the sum of three elements and divided by a value which is given as an input by the user
x=int(input("Enter 1 number :"))
y=int(input("Enter 2 number :"))
z=int(input("Enter 3 number :"))
s=x+y+z
print("The sum \"s\" is:")
print(s)
a=int(input("Enter number to divide:"))
if s% a==0:
    print("The given inputs are divided by value")
else :
    print("The given inputs do not  get divided by value")



print()
#8) Write a Python program to find the Mean,median,mode among three given numbers

def MMM(n_num):
    n = len(n_num)
    get_sum = sum(n_num)
    mean = get_sum / n
    print("Mean / Average is: " + str(mean))
    n_num.sort()
    if n % 2 == 0:
        median1 = n_num[n//2]
        median2 = n_num[n//2 - 1]
        median = (median1 + median2)/2
    else:
        median = n_num[n//2]
    print("Median is: " + str(median))
    data = Counter(n_num)
    get_mode = dict(data)
    mode = [k for k, v in get_mode.items() if v == max(list(data.values()))]
    if len(mode) == n:
        get_mode = "No mode found"
    else:
        get_mode = "Mode is / are: " + ', '.join(map(str, mode))
    print(get_mode)

print()
#9)Write a Python program to swap cases of a given string
x = "Git"
y = "HUB"
print("Before:")
print(x,y)
x, y = y, x
print("after:")
print(x,y)



#10) Write a program to convert an integer to binary & octa decimal
#octa decimal
def dectooctal(n):
    octNum = [0] * 100
    i = 0
    while (n != 0):
        octNum[i] = n % 8
        n = int(n / 8)
        i += 1
    for j in range(i - 1, -1, -1):
        print(octNum[j], end="")

dectooctal(8)