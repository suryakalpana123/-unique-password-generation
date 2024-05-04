import random
import string

def generate_password(length):
    # Define the character set for the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password using the defined character set
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

if __name__ == "__main__":
    # Set the desired length of the password
    password_length = int(input("enter the length for your password:"))
    
    # Generate a random password
    password = generate_password(password_length)
    
    # Print the generated password
    print("Generated Password:", password)
