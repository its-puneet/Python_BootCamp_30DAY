 #1)	Write a program to create a list of n integer values and do the following
n=5
list_items=[]
for i in range(n):
    a=int(input())
    list_items.append(a)
print("The list is:")
print(list_items)

# •	Add an item in to the list (using function)
list_items.append(30)
print("The list after adding an item to the list using functions:")
print(list_items)

# •	Delete (using function)
print()
list_items.remove(15)
print("List after using item to remove from list:")
print(list_items)

print()
print("List after using index to remove from list:")
list_items.pop(2)
print(list_items)

print()
# •	Store the largest number from the list to a variable
x=max(list_items)
print("The largest number is:")
print(x)
# •	Store the Smallest number from the list to a variable
print()
y=min(list_items)
print("The smallest number is:")
print(y)
print()

# 2) Create a tuple and print the reverse of the created tuple
p =(5,8,2,4,9,1)
w=sorted(p)
print("Before sorting:",p)
print("Sorted tupl:",w)
print("Reversed tuple: ",sorted(w,reverse=True))

# 3) Create a Tuple And Convert into List

t =(5,2,4,9,8,7,6,3)
list_1=list(t)
print("Tuple: ",t)
print()
print("Tuple as list: ",list_1) 