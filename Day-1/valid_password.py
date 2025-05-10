
def valid_password(password):
    number_present = False
    special_character = False
    alphabet_present = False
    upper_case = False
    for char in password:
        if char.isdigit():
            number_present = True
        if char.isalpha():
            alphabet_present = True
            if char.isupper():
                upper_case = True
        if not char.isalnum():
            special_character = True
    if number_present and special_character and alphabet_present and upper_case and len(password)>6:
        print('Valid Password')
    else:
        print('Invalid password')

password = input()
valid_password(password)