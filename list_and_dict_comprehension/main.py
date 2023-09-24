# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# new_numbers = [n**2 for n in numbers]
# print(new_numbers) 

# names = ['Alex', 'Maya', 'Jasmin', 'Margot']
# import random
# student_scores = {name: random.randint(1,100) for name in names}
# print(student_scores)
# passed_students = {name:score for (name,score) in student_scores.items() if score > 60}
# print(passed_students)

#sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
#s_list = sentence.split()
#dict = {word:len(word) for word in sentence.split()}
#print(dict)
#--------------------------------------------------------------
# temp_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }

# def convert_to_f(temp):
#     temp_f = temp * (9/5) + 32
#     return temp_f

# f = {day:convert_to_f(temp) for (day,temp) in temp_c.items()}
# print(f)
#-----------------------------------------------------------------
import pandas as pd

student_data = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98],
}

student_data_frame = pd.DataFrame(student_data)
print(student_data_frame)

for (index, row) in student_data_frame.iterrows():
    print(row)
    print(row.student) #as each row is a serie