import math

#1) Write a program to loop through a list of numbers and add +2 to every value to elements in list

l=[0,2,4,6,8,10]
r=[]
for i in l:
    r.append(i+2)
print(r)

print()
'''2)Write a program to get the below pattern
54321
4321
321
21
1'''

for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j,end=' ')
    print()

print()
#3)Python Program to Print the Fibonacci sequence
#using recursion
def Fib(n):
    if n < 0:
        print("input is negatuve")
    elif n == 1 or n == 2:
        return 1
    else:
        return Fib(n-1) + Fib(n-2)
print(Fib(5))

print()
'''4) Explain Armstrong number and write a code with a function
Armstrong number is a number whose digits cube is equals to the same number. Eg: | 153 | but how?? 1*1*1=1, 5*5*5=125 ,3*3*3=27, 1+125+27=153'''

n = int(input("Enter number: "))
s = 0
t = n
while t > 0:
    one = t % 10
    s += one**3
    t //= 10
if n == s:
    print(n,"is an Armstrong number")
else:
    print(n,"is not an Armstrong number")

print()
#5)Write a program to print the multiplication table of 9
print("The multiplication table of 9 is:")
for i in range(1,11):
    print("9x",i,"=",i*9)


print()
#6)Check if a program is negative or positive
l=[-6,4,7,-1,4,8]
for i in l:
    if i >=0:
        print(i," is positive")
    else :
        print(i,' is negative ')
print()
#7)Write a program to convert the number of days to ages

def find(number_of_days):
    year = int(number_of_days / 365)
    print(year,'Years =',number_of_days,'days')

find(365)
print()
#8) Solve Trigonometry problem using math function write a program to solve using math function


def trigno(n,m):
    if n=='sin':
        return math.sin(m)
    elif n=='cos':
        return math.cos(m)
    elif n=='cosin':
        return math.cosine(m)
    elif n=='tan':
        return math.tan(m)
    elif n=='sec':
        return math.sec(m)
    elif n=='cosec':
        return math.cosec(m)

trigno('sin', 90)

print()
#9) create a basic calculator using if condition only
def calculator():
    print("Enter first number:")
    number_1 = int(input())
    print("Enter second number:")
    number_2 = int(input())
    print('1. Add: \'+\'')
    print('2. Sub: \'-\'')
    print('3. Multiply: \'*\'')
    print('4. Divide:\'/\'')
    print('5. Mod: \'%\'')
    print('6. Power: \'**\'')
    op = input("Select your operator: ")
    

    if op == '+': 
        print(number_1 + number_2)
    elif op == '-':
        print(number_1 - number_2)
    elif op == '*': 
        print(number_1 * number_2)
    elif op == '/':
        print(number_1 / number_2)
    elif op == '%': 
        print(number_1 % number_2)
    elif op == '**': 
        print(number_1 ** number_2)
    else:
        print('Invalid Inputs')

calculator()