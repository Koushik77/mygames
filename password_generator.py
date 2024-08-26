import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_length = nr_letters + nr_symbols + nr_numbers
password = ''

pwd_letters = []
pwd_symbols = []
pwd_numbers = []

for i in range(0, nr_letters):
    pwd_letters.append(letters[random.randint(0, len(letters) -1)])
for i in range(0, nr_symbols):
    pwd_symbols.append(symbols[random.randint(0, len(symbols) -1)])
for i in range(0, nr_numbers):
    pwd_numbers.append(numbers[random.randint(0, len(numbers) -1)])

#print(pwd_letters, pwd_symbols, pwd_numbers)
for i in range(0, password_length):
    char_type = random.randint(0, 2)
    if char_type == 0 and len(pwd_letters) > 0:
        letter_index = random.randint(0, len(pwd_letters) -1)
        password += pwd_letters[letter_index]
        pwd_letters.pop(letter_index)
    elif char_type == 1 and len(pwd_symbols) > 0:
        symbol_index = random.randint(0, len(pwd_symbols) -1)
        password += pwd_symbols[symbol_index]
        pwd_symbols.pop(symbol_index)
    elif char_type == 2 and len(pwd_numbers) > 0:
        number_index = random.randint(0, len(pwd_numbers) -1)
        password += pwd_numbers[number_index]
        pwd_numbers.pop(number_index)
    else:
        if len(pwd_letters) > 0:
            letter_index = random.randint(0, len(pwd_letters) - 1)
            password += pwd_letters[letter_index]
            pwd_letters.pop(letter_index)
        elif len(pwd_symbols) > 0:
            symbol_index = random.randint(0, len(pwd_symbols) - 1)
            password += pwd_symbols[symbol_index]
            pwd_symbols.pop(symbol_index)
        elif len(pwd_numbers) > 0:
            number_index = random.randint(0, len(pwd_numbers) - 1)
            password += pwd_numbers[number_index]
            pwd_numbers.pop(number_index)

print(password)
