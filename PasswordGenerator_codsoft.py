import random
import string

# Function to generate a random password
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Prompt user for desired password length
try:
    password_length = int(input("Enter the desired length of the password: "))
    if password_length <= 0:
        print("Invalid input. Please enter a positive integer.")
    else:
        # Generate and display the password
        generated_password = generate_password(password_length)
        print("Generated Password: ", generated_password)
except ValueError:
    print("Invalid input. Please enter a valid integer for password length.")