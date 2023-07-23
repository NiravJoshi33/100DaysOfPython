#Welcome to Odd-Even Detector

#Get input
a = float(input("Enter the number:"))

#Check if the number is odd or even
if (a%2)==0 :   #if the remainder of the division of the number by 2 is zero, then the number is even
    print(f"The number {a} is even")
else:
    print(f"The number {a} is odd")