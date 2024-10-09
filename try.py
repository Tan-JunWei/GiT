# Inputs
p = 53
q = 97
e = 65537
message = "!L0VEH@RRYP0TTER"

# RSA modulus
n = p * q

# Function to calculate RSA encryption and sum of digits
def encrypt_and_hash(char, e, n):
    ascii_value = ord(char)
    padded_value = ascii_value + 1000
    encrypted_value = pow(padded_value, e, n)
    # Sum of digits as the hash function
    digit_sum = sum(int(digit) for digit in str(encrypted_value))
    return digit_sum

# Apply the encryption and hash function to each character in the message
encrypted_hashes = [encrypt_and_hash(char, e, n) for char in message]

# Construct the flag format
flag = "GIT{" + "_".join(map(str, encrypted_hashes)) + "}"
print(flag)
