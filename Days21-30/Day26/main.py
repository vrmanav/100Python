# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 78, 98],
# }
# result_DF = pd.DataFrame(student_dict)
# result_DF.to_csv("./output.csv", index=False)

# for index, row in result_DF.iterrows():
#     print(row.student)

import pandas as pd

file = pd.read_csv("./nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for index, row in file.iterrows()}

name = input("Enter your name:\n").upper()

output_list = [nato_dict[letter] for letter in name]
print(output_list)
