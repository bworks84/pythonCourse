# encryption psuedo code
# initialize output string variable
# loop for number of characters in the string
#   get ordinal value of input character
#   calculate the offset
#   (account for wrap)
#   add the adjusted offset to the value
#   append character to output string
# return the output string

# Notes:
#   ord() = returns the unicode from a give character
#   chr() = returns a string representing a char whose unicode is the integer specified

def caesar_Encrypt(input_message, encryption_key):
    output_string = ""
    for letter in input_message:
        letter_value = ord(letter)
        letter_value = letter_value + encryption_key
        if letter_value > 126:
            letter_value = letter_value - 95
        elif letter_value < 32:
            letter_value = letter_value + 95
        output_string = output_string + chr(letter_value)
    return output_string


# Main program
# input a string
print("Secret Message Encoder")
print("----------------------")
input_message = input("Enter a message to be encoded\n")

# input an encryption key (how many letters to move)
key = int(input("What is the encryption key?\n"))

# encrypt the string
encrypted_string = caesar_Encrypt(input_message, key)

# print the encrypted string
print("Encrypted string: ", encrypted_string)


# print the reverse-encrypted string
reverse_encrypted_string = caesar_Encrypt(encrypted_string, -key)
print("Decrypted string: ", reverse_encrypted_string)
