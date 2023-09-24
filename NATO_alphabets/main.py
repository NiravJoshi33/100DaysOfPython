student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas as pd
#student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
alphabet_data = pd.read_csv("NATO_alphabets/nato_phonetic_alphabet.csv")
alphabet_dataframe = pd.DataFrame(alphabet_data)
#print(alphainbet_dataframe)

alphabet_dict = {row.letter: row.code for (index, row) in alphabet_dataframe.iterrows()}
#print(alphabet_dict)
    
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter the word:").upper()
#user_input_list = [a for a in user_input]
code_list = [alphabet_dict[letter] for letter in user_input]    
print(code_list)
