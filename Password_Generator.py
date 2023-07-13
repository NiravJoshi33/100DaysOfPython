#Password Generator

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Now there are two levels of this project: Eazy and Hard. In Eazy level, the password will be generated in order and in Hard mode, the password will be generated in random order

#Eazy Password
n = len(letters)
password = ""
for times in range (1,nr_letters+1):
    r_num = random.randint(0,n-1)
    password = password + letters[r_num]
    #print(password)

n = len(numbers)
for times in range (1,nr_numbers+1):
    r_num = random.randint(0,n-1)
    password = password + numbers[r_num]
    #print(password)

n = len(symbols)
for times in range (1,nr_symbols+1):
    r_num = random.randint(0,n-1)
    password = password + symbols[r_num]
    #print(password)

print(f"Eazy password: {password}")

l = list(password) #shuffle function can be applied to lists only so we are converting string to lists
#print(l)
random.shuffle(l)
#print(l)
password = "".join(l) #This is alternatively possible using for loop and adding each element to the string
print(f"Hard Password: {password}")