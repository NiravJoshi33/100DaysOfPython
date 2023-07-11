#This is a tutorial of the nested lists

#dirty dozen: list of fruits and vegetables with the most pestisides

#dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"] #List without nesting

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes"]
vegetables = ["Spinach", "Kale", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]  #dirty_dozen is a nested list of list "fruits" and "vegetables"

print(dirty_dozen)