programming_dictionary = {
    "Bug": "An error in program that prevents the program from running as expected",
    "Function": "A piece of code that you can call over and over again",
    "Loop": "The action of doing something over and over again"
}

print(programming_dictionary["Bug"]) #here the value is extracted using a key

#Adding new iteam to the dictionary
programming_dictionary["variable"] = "Varianbles are used to store value in the memory and to be used again and again in the program"

print(programming_dictionary)

#Create an empty dictionary
empty_dictionary = {}

#wipe the existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

#Edit the element in the dictionary
programming_dictionary["Bug"] = "A moth in your computer"
print(programming_dictionary)

#Loop through dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])