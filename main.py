from data import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def cipher(push_num, msg, converter):
    new_msg = ""
    if converter == "encode":
        for letter in msg:
            if letter in alphabet:
                index = alphabet.index(letter)
                new_msg += alphabet[index + push_num]
            elif letter == " ":  # for spaces
                new_msg += " "
            else:  # for emojis
                new_msg += letter

    elif converter == "decode":
        for letter in msg:
            if letter in alphabet:
                index = alphabet.index(letter)
                new_msg += alphabet[index - push_num]
            elif letter == " ":  # for spaces
                new_msg += " "
            else:  # for emojis
                new_msg += letter

    return new_msg


is_on = True
print(logo)
while is_on:
    user_input = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
    message = input("Type your message: ")
    shift_num = int(input("Enter shift Number: "))

    if 0 <= shift_num < 26:
        output = cipher(shift_num, message, user_input)
        print(f"RESULT = {output}")
    else:
        print("Invalid Shift Number")

    go_on = input("Type 'yes' if you want to go again. Otherwise type 'no': ")

    if go_on == "no":
        is_on = False
