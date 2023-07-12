#Divide a two digit number in two numbers

num = input("Enter the value of the number: ")

#split
#first = int(num/10)
#second = num - (first*10)

#alternatively since input is string, the values can be extracted using a sting array as well
first = num[0]
second = num[1]


print(f"First value is {first}")
print(f"Second value is {second}")