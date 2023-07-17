# Coffee Machine code

data = {

        'Espresso':{'Water': 50,'Coffee': 18,'Milk': 0,'Price': 1.5},
        'Latte':{'Water': 200,'Coffee': 24,'Milk': 150,'Price': 2.5},
        'Cappuccino':{'Water': 250,'Coffee': 24,'Milk': 100,'Price': 3}
}

# Prompt to ask customer which coffee they would like to have
coffee_type = input('What would you like? (Espresso/ Latte/ Cappuccino)\n')

# Input available resources
available_water = 500
available_coffee = 100
avaialable_milk = 600

def check_resources(coffee_type1):
    req_water1 = data[coffee_type1]['Water']
    req_coffee1 = data[coffee_type1]['Coffee']
    req_milk1 = data[coffee_type1]['Milk']
    #print(req_water)
    #print(req_coffee)
    #print(req_milk)

    if req_water1 < available_water and req_coffee1 < available_coffee and req_milk1 < avaialable_milk:
        return True
    else:
        return False
        print("Not sufficient Ingredients")

#coffee_type1 = ""
def make_coffee(coffee_type1):
    available_water1 = available_water - data[coffee_type1]['Water']
    available_coffee1 = available_coffee - data[coffee_type1]['Coffee']
    avaialable_milk1 = avaialable_milk - data[coffee_type1]['Milk']
    next = input("Here is your coffee. Please press enter after taking your coffee: ")
    return(available_water1, available_coffee1, avaialable_milk1)

proceed = check_resources(coffee_type)

while proceed == True:
    (available_water, available_coffee, avaialable_milk)= make_coffee(coffee_type)
    print(f"remaining resources: Water = {available_water}, Coffee = {available_coffee}, Milk = {avaialable_milk}")
    coffee_type = input('What would you like? (Espresso/ Latte/ Cappuccino)\n')
    proceed = check_resources(coffee_type)
    
print("Coffee machine is out of ingredients")
    
