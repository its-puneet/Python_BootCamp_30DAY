# It does not matter you use single quotes or double quotes in python
print("30 days 30 hour challenge")
#Output:
print('30 days 30 hour challenge')
#Output:30 days 30 hour challenge

#Assigning values to variables
Hours = "thirty" #here hours is a variable assigned value of a string "thirty"
print(Hours)
#Output: thirty

""" Indexing using String:
indexing starts from 0 """
Days = "Thirty days"
print(Days[0])
print(Days[1])
print(Days[2])
print(Days[3])
print(Days[4])
print(Days[5])
print(Days[6])
print(Days[7])
print(Days[8])
print(Days[9])


#How to print the particular character from certain text? 
Challenge = "I will eat"
print(Challenge[7:10])



#Print the length of Character:
Challenge = "I am a boy"
print(len(Challenge))


#Convert String into lower and upper character;
Challenge = "I Am a BOY"
print(Challenge.lower())
print(Challenge.upper())


#String Concatenation – Joining two strings
a = "30 Days"
b = "30 hours"
c = a + b
print(c)
#Adding space during concatenation
a = "30 Days"
b = "30 hours"
c = a + " " + b
print(c)


#casefold() - Usage
text = "Thirty days and Thirty hours"
x = text.casefold()
print(x)

#Capitalize the first letter in this sentence
y=text.capitalize()
print(y)

#used to find a word in the sentence
z=text.find("and")
print(z)

#returns True if all the characters are alphabet letters (a-z)
r=text.isalpha()
print(r)

#returns True if all the characters are alphanumeric, meaning alphabet letter (a-z) and numbers (0-9).
s=text.isalnum()
print(s)

