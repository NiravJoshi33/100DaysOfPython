#Welcome to the tip calculator
total_bill = input("Enter the total bill amount:")
persons = input("Enter the no. of person to split the bill for:")
per = input("Enter the percentage of the tip you would like to add:")
final_bill = (float(total_bill)/float(persons))*(1+(float(per)/100)) #here we have used float function to convert strings to float values explicitely
print("You have to pay " + str(round(final_bill, 2)) + " rupees") #here we have used str to convert float function to convert float values to string explicitely