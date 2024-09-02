import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["$", "!", "@", "#", "%", "^", "&", "*", "(", ")", "=", "_"]

print("Welcome to password generator")
characters = int(input("How many characters do you want in your password?"))
numbers = int(input("How many numbers do you want in your password?"))
numSymbols = int(input("How many symbols do you want in your password?"))

letterRem = characters - numbers - numSymbols

randomCharacters = ""
password = ""
for number in range(1, letterRem):
    randomCharacters += random.choice(letters)

for number in range(1, numbers + 1):
    randomCharacters += random.choice(digits)

for number in range(1, numSymbols + 1):
    randomCharacters += random.choice(symbols)

for number in range(1, characters + 1):
    password += random.choice(randomCharacters)

print(password)
