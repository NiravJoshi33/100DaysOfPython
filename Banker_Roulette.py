import random

#input the names
n_string = input("Enter the name of people separated by comma and space:") #here we are using comma and space as a trimming tool that separates different names

#split the string into list
names = n_string.split(", ") #split command splits the string by the mentioned characters and converts into a list

#find a random name
no_of_people = len(names)   #find the no. of elements inside the list
random_number = random.randint(1,no_of_people-1)    #generate a random number between 1 and no. of elements
payer = names[random_number]    #find a name associated with the random number

print(payer + " will pay the bill today!")