import random 
import string

length = int(input("Enter the length of the password: "))
include_numbers = input("include numbers? (y/n): ").lower() == 'y'
include_special_chars = input("include special characters? (y/n): ").lower() == 'y'

characters = string.ascii_letters
if include_numbers:
    characters += string.digits
if include_special_chars:
    characters += string.punctuation

password = ''.join(random.choice(characters) for _ in range(length))
print("---------------------------------")
print("Generated password:", password)
save_to_file = input("Do you want to save the password to a file? (y/n): ").lower() == 'y'
if save_to_file:
    with open("password.txt", "w") as file:
        file.write(password)
    print("Password saved to password.txt")
input("Press Enter to exit...")
