# Coffee Machine code

data = {

        'Espresso':{'Water': 50,'Coffee': 18,'Milk': 0,'Price': 1.5},
        'Latte':{'Water': 200,'Coffee': 24,'Milk': 150,'Price': 2.5},
        'Cappuccino':{'Water': 250,'Coffee': 24,'Milk': 100,'Price': 3}
}

# Input available resources
available_water = 500
available_coffee = 100
avaialable_milk = 600
Money = 0

# Prompt to ask customer which coffee they would like to have
coffee_type = input('What would you like? (Espresso/ Latte/ Cappuccino)\n')

def report():
    print("Available resources: ")
    print(f"Water = {available_water}")
    print(f"Coffee = {available_coffee}")
    print(f"Milk = {avaialable_milk}")
    print(f"Money = {Money}")


def check_resources(coffee_type1):
    req_water1 = data[coffee_type1]['Water']
    req_coffee1 = data[coffee_type1]['Coffee']
    req_milk1 = data[coffee_type1]['Milk']
    #print(req_water)
    #print(req_coffee)
    #print(req_milk)

    if req_water1 < available_water and req_coffee1 < available_coffee and req_milk1 < avaialable_milk:
        return True
    if req_water1 > available_water:
        return("water")
    if req_coffee1 > available_coffee:
        return("coffee")
    if req_milk1 > avaialable_milk:
        return("milk")


#coffee_type1 = ""
def make_coffee(coffee_type1):
    available_water1 = available_water - data[coffee_type1]['Water']
    available_coffee1 = available_coffee - data[coffee_type1]['Coffee']
    avaialable_milk1 = avaialable_milk - data[coffee_type1]['Milk']
    next = input("Here is your coffee. Please press enter after taking your coffee: ")
    return(available_water1, available_coffee1, avaialable_milk1)

def collect_money(coffee_type1):
    print("Please insert the coins:\n")
    quarters = float(input("Please enter no. of quarters:"))
    dimes = float(input("Please insert no. of dimes: "))
    nickles = float(input("Please insert no. of nickles: "))
    pennies = float(input("Please insert no. of pennies: "))
    total_coin_value = (quarters*0.25) + (dimes*0.1) + (nickles*0.05) + (pennies*0.01)
    return(total_coin_value)

if coffee_type == "report":
    report()
else:
    proceed = check_resources(coffee_type)

while proceed == True:
    inserted_coins_value = collect_money(coffee_type)
    while inserted_coins_value < data[coffee_type]['Price']:
        print("You have inserted insufficient coins: ")
        print("Here is your money back & please insert the sufficient amount now:")
        inserted_coins_value = collect_money(coffee_type)
    print(f"You have inserted total {inserted_coins_value}")
    return_change = inserted_coins_value - data[coffee_type]['Price']
    Money = Money + data[coffee_type]["Price"]
    print(f"Here is the change: {return_change}")
    (available_water, available_coffee, avaialable_milk)= make_coffee(coffee_type)
    print(f"remaining resources: Water = {available_water}, Coffee = {available_coffee}, Milk = {avaialable_milk}")
    coffee_type = input('What would you like? (Espresso/ Latte/ Cappuccino)\n')
    if coffee_type == "report":
        report()
    else:
        proceed = check_resources(coffee_type)
    
print(f"We are out of {proceed}")
    
