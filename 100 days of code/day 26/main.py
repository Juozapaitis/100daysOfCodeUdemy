import random
import pandas

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
# name = "Angela"
# letters_list = [letter for letter in name]
# print(letters_list)

# doubled_list = [i*2 for i in range(1,5) if i % 2 == 0]
# print(doubled_list)

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# for (key, value) in student_dict.items():
#     print(key)

student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

# Loop through rows of a data frame

for (index, row) in student_data_frame.iterrows():
    print(row)