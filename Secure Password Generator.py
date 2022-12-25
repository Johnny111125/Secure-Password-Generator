import random
import string

def generate_password(length=12):
    """Generate a random, secure password of the specified length.
    
    The password will contain a mix of lowercase letters, uppercase letters,
    numbers, and special characters.
    
    Args:
        length (int): The desired length of the password.
        
    Returns:
        str: The generated password.
    """
    # Use the string module's ascii_letters and digits constants to get
    # a list of all lowercase letters, uppercase letters, and digits.
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Use the random module's sample function to randomly select characters
    # from the list of characters to create the password.
    password = ''.join(random.sample(characters, length))
    
    return password

# Generate a password of length 12 (the default length)
password = generate_password()
print(password)
