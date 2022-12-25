# Secure-Password-Generator

This code defines a function generate_password that generates a random, secure password of the specified length. The password will contain a mix of lowercase letters, uppercase letters, numbers, and special characters.

The function uses the string module's ascii_letters and digits constants to get a list of all lowercase letters, uppercase letters, and digits. It then uses the random module's sample function to randomly select characters from this list to create the password.

The default length of the password is 12 characters, but the user can specify a different length by passing a value for the length parameter.

The code at the end of the script generates a password of length 12 (the default length) and prints it to the console.
