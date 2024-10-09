import string
encrypted_message = "Cpud lXypuQkaZ@c neoHculetd .ceqjzpanqpzhra"
caesar_shift = 88
vigenere_key = "IWANTMAGICPoints"
special_numbers = [55.4156, -1.7059]

keyword = "ALNWICK" #1567324
columns = []

for i in range(0, len(encrypted_message), 7):
    columns.append(encrypted_message[i:i+7])

