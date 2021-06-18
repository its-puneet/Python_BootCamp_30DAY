""" 1. Create a function getting two integer inputs from user.& print the following:
Addition of two numbers is +value
Subtraction of two numbers is +value
Division of two numbers is +value
Multiplication of two numbers is +value
Here the value represents math function associated """


a= int(input("Enter first number:"))
b=int(input("Enter second number: "))
print("Enter:")
print( "1. '+' for Addition , 2. '-' for Subration , 3. '*' for Multiplication, 4. '/ for Division'")
s=input()

print()
def math(a,b,sign):
    if sign == '+':
        print("a + b : ",str(a+b))
    elif sign == '-':
        print("a - b : ",str(a-b))
    elif sign == '*':
        print("a * b : ",str(a*b))
    elif sign == '/':
        print("a / b : ",str(a/b))

math(a,b,s)

print()
#2. Create a function covid( ) & it should accept patient name, and body temperature, by default the body temperature should be 98 degree
patient_name=input("Enter patient name :")
body_temp=input("enter body temprature : ")

def covid(patient_name,body_temp):
    print("Name of patient: ",patient_name)
    if body_temp == '':
        print("Body Temprature :98 degrees")
    else:
        print("Body Temprature :",body_temp, "degrees")
covid(patient_name,body_temp)
