text = str(input('Enter the String '))
shift= int(input('Shift '))
def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Only process alphabetic characters
            base = ord('A') if char.isupper() else ord('a')
            shifted_char = chr((ord(char) - base + shift) % 26 + base)
            encrypted_text += shifted_char
        else:
            encrypted_text += char  # Keep non-alphabetic characters unchanged
    return encrypted_text

# Example usage
plaintext = "wipro"
shift_value = 1
encrypted_message = caesar_encrypt(text, shift)
print("Encrypted message:", encrypted_message)
