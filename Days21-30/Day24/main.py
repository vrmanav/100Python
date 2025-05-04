# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


formatted_list = []

with open("./invitees.txt", mode="r") as invitees:
    original_list = invitees.readlines()
    for person in original_list:
        name = person.strip()
        formatted_list.append(name)

with open("./format.txt", mode="r") as format:
    letter_str = format.read()
    for name in formatted_list:
        letter = letter_str.replace("[name]", name)
        with open(f"./ReadyToSend/letter_for_{name}", mode="w") as final_letter:
            final_letter.write(letter)
