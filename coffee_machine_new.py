# Below is the data associated with the different type of coffee. We have created this as dictionary as it is easier for us to use input as parameter to extract this data
data = {

        'Espresso':{'Water': 50,'Coffee': 18,'Milk': 0,'Price': 1.5},
        'Latte':{'Water': 200,'Coffee': 24,'Milk': 150,'Price': 2.5},
        'Cappuccino':{'Water': 250,'Coffee': 24,'Milk': 100,'Price': 3}
}

# Input available resources
available_water = 500
available_coffee = 100
available_milk = 600
Money = 0

def report():
    print("Please find the below report:")
    print(f"Available Water = {available_water}")
    print(f"Available Coffee = {available_coffee}")
    print(f"Available Milk = {available_milk}")
    print(f"Collected Money = {Money}")

def check_res(coffee1):
    req_water1 = data[coffee1]['Water']
    req_coffee1 = data[coffee1]['Coffee']
    req_milk1 = data[coffee1]['Milk']

    if req_water1 < available_water and req_coffee1 < available_coffee and req_milk1 < available_milk:
        return True
    if req_water1 > available_water:
        return("water")
    if req_coffee1 > available_coffee:
        return("coffee")
    if req_milk1 > available_milk:
        return("milk")

def process_coins(coffee3):
        print(f"Please insert the coins, the required amount is {data[coffee3]['Price']}:\n")
        quarters = float(input("Please enter no. of quarters:"))
        dimes = float(input("Please insert no. of dimes: "))
        nickles = float(input("Please insert no. of nickles: "))
        pennies = float(input("Please insert no. of pennies: "))
        total_coin_value = (quarters*0.25) + (dimes*0.1) + (nickles*0.05) + (pennies*0.01)
        return(total_coin_value)

def make_coffee(coffee2):
    available_water1 = available_water - data[coffee2]['Water']
    available_coffee1 = available_coffee - data[coffee2]['Coffee']
    available_milk1 = available_milk - data[coffee2]['Milk']
    next = input(f"Here is your {coffee2}. Enjoy! ")
    return(available_water1, available_coffee1, available_milk1)

cont = True
collected_coins = 0

while cont == True:
    coffee = input("What would you like? (espresso/ latte/ cappuccino): ").title()
    #print(f"You have entered {coffee}")
    if coffee == "Report":
        report()
    elif coffee == "Off":
        cont = False
    elif coffee == "Espresso" or coffee == "Latte" or coffee == "Cappuccino":
        res = check_res(coffee)
        print("resources checked")
        if res == "water":
            cont = False
            print("Sorry, We are out of water")
        elif res == "coffee":
            cont = False
            print("Sorry, We are out of coffee")
        elif res == "milk":
            cont = False
            print("Sorry, We are out of milk")
        elif res == True:
            collected_coins = process_coins(coffee)
            while collected_coins < data[coffee]['Price']:
                print("Entered amount is insufficient. Please collect your refund.")
                print("Please insert the coins again:")
                collected_coins = process_coins()
            if collected_coins > data[coffee]['Price']:
                return_coins = collected_coins - data[coffee]['Price']
                print(f"Please collect your change: {return_coins:.2f}")
            Money = Money + data[coffee]['Price']
            (available_water, available_coffee, avaialable_milk)= make_coffee(coffee)
    else:
        cont = False
        print("You have entered invalid input")
    


