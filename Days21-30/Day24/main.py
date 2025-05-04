PLACEHOLDER = "[name]"

with open("./invitees.txt", mode="r") as guest_names:
    names = guest_names.readlines()

with open("./format.txt", mode="r") as format:
    letter_str = format.read()
    for name in names:
        formatted_name = name.strip()
        letter = letter_str.replace("[name]", formatted_name)
        with open(f"./ReadyToSend/letter_for_{name}", mode="w") as final_letter:
            final_letter.write(letter)
