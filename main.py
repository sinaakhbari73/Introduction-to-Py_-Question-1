# Define the encrypt function.
def encrypt(text, key):
    encrypted = ""  # Initialize an empty string.
    for char in text:  # Loop.
        if char.isalpha():  # Check if the character is a letter.
            shift = key if char.islower() else -key # Determine the direction of the shift.
            char_code = ord(char.lower()) # Our Converter.
            encrypted += chr((char_code + shift - 97) % 26 + 97).upper() if char.isupper() else chr(
                (char_code + shift - 97) % 26 + 97)
        else:
            encrypted += char  # If the character is not a letter, result without changing.
    return encrypted  # Return the result.


# Define the decrypt function.
def decrypt(text, key):
    return encrypt(text, -key)  # Call the encrypt function.


# Main function.
def main():
    # Ask the user if they want to encrypt or decrypt.
    choice = input("Do you want to (e)ncrypt or (d)ecrypt?\n> ")

    # Ask for the key to use for the Caesar Cipher.
    key = int(input("Please enter the key (0 to 25) to use.\n> "))

    # Ask for the message to encrypt/decrypt.
    message = input("Enter the message to {}.\n> ".format("encrypt" if choice == 'e' else "decrypt"))
    if choice == 'e':  # If the user chooses to encrypt.
        encrypted_message = encrypt(message, key)  # Encrypt the message.
        print("Fully encrypted text copied to clipboard:\n{}".format(encrypted_message))  # Display.
    else:  # If the user chooses to decrypt.
        decrypted_message = decrypt(message, key)  # Decrypt the message.
        print("Fully decrypted text copied to clipboard:\n{}".format(decrypted_message))  # Display.


if __name__ == "__main__":
    main()  # End
