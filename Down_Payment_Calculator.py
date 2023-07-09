#Weloome to Down Payment Calculator

#Reference for the theory: https://cleartax.in/s/down-payment-calculator#:~:text=For%20example%2C%20you%20want%20to,00%2C000%20*%200.01%20%3D%20Rs%2040%2C000.

#Ask for the input values
House_Value = input("Enter the value of the house in rupees:")
down = input("Enter the percentage of down payment you'd like to make:")
processing_fees = 1 #processing fee on remaining amount in percentage
H_down_amount = (float(House_Value)*float(down)/100)
years = float(input("Enter total loan period in years:")) #here instead of converting the value into float multiple times in other expression, we converted it at the time of assignment only. 
months = years*12
Rate = 10 #rate of interest set by the bank

#Calculate & display the amount required at the time of down payment
print("You want to do down payment of " + str(H_down_amount) + " rupees")
F_down_amount = float(H_down_amount) + (float(House_Value)-float(H_down_amount))*(float(processing_fees)/100)
print("You will need " + str(F_down_amount) + " rupees for down payment")
print("Your load period in months is " + str(months))

#Calculate EMI and display it to the customer
EMI = (float(House_Value)-float(H_down_amount))*(Rate/100/12)*((1+(Rate/100/12))**months)/(((1+(Rate/100/12))**(months))-1)
#print("Your monthly EMI amount is" + str(round(EMI,2)) + " rupees")
#f-string - instead of converting all the different data types to str again and again we can use f-string
print(f"Your monthly EMI amount is {round(EMI, 2)}")

#Calculate total amount paid by customer at the end of their loan period
#T_incurred_cost = EMI*months + F_down_amount
#print(f"Customer has paid total {T_incurred_cost} rupees at the end of {months} months" )
#print("You have paid "+ str(round((T_incurred_cost - float(House_Value)),2)) + " rupees extra")