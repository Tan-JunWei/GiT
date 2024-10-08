import string

encrypted_string = "S vyfo Robwsyxo Qbkxqob!"
shift = 10
decrypted = ""
uppercase = string.ascii_uppercase
lowercase = string.ascii_lowercase

for char in encrypted_string:
    if char in uppercase:
        index = uppercase.find(char)
        decrypted += uppercase[(index - shift) % 26]
    elif char in lowercase:
        index = lowercase.find(char)
        decrypted += lowercase[(index - shift) % 26]
    else:
        decrypted += char

print(decrypted)