# Caesar Cipher

alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

# !Noob approach
# def encode(original_text, shift):
#     """Encodes the text provided by the user"""
#     ciphered_text = ""
#     for letter in original_text:
#         old_index = alphabet.index(letter)
#         new_index = (old_index + shift) % 26
#         new_letter = alphabet[new_index]
#         ciphered_text += new_letter
#     print(f"\nEncoded text is - {ciphered_text}")

# def decode(original_text, shift):
#     """Decodes the text provided by the user"""
#     ciphered_text = ""
#     for letter in original_text:
#         old_index = alphabet.index(letter)
#         new_index = (old_index - shift) % 26
#         new_letter = alphabet[new_index]
#         ciphered_text += new_letter
#     print(f"\nDecoded text is - {ciphered_text}")


# !Improved approach
def cipher(original_text, shift, choice):
    """Encodes or decodes original text based on user's choice and returns the ciphered text"""
    if choice == "decode":
        shift *= -1
    ciphered_text = ""
    for letter in original_text:
        if letter in alphabet:
            old_index = alphabet.index(letter)
            new_index = (old_index + shift) % 26
            new_letter = alphabet[new_index]
            ciphered_text += new_letter
        else:
            ciphered_text += letter
    return ciphered_text


def caesar_cipher():
    """Start caesar cipher"""
    print("Welcome to Caesar Cipher 🔐\n")
    choice = input(
        "Do you want to encode or decode your text [ENCODE/DECODE]: "
    ).lower()
    original_text = input("Enter your text: ").lower()
    shift = int(input("Enter shift number: "))

    # !Part of noob approach
    # if choice == "encode":
    #     encode(original_text=original_text, shift=shift)
    # elif choice == "decode":
    #     decode(original_text=original_text, shift=shift)

    ciphered_text = cipher(original_text=original_text, shift=shift, choice=choice)
    print(f"\n{choice.capitalize()}d text is: {ciphered_text}")


caesar_cipher()
