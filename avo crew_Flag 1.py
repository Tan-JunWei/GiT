# At Gringotts Wizarding Bank, powerful sorcerers store their most precious artifacts at vault 713,
# protected by a secret code known only to them. However, to keep the code safe from dark
# wizards, masking spells are being cast on the code to hide all characters with a “*” except for
# the last 4.

# As an apprentice of the keeper, your task is to cast the spell (write out the code)
# masking_spell(code) that hides all characters with a “*” except for the last 4.

# However, if the code has less than 8 characters, the message “Unstable code” would be sent
# out as the code is too weak to protect the code. 
# If the code ends with a vowel (a/e/i/o/u), “- Dark
# Magic Detected” would be added to the masked code. Your flag should look like this:
# GIT{masked_code}

string1 = "AUC8EH"
string2 = "ZY12QHPO94TR"
string3 = "ZY12QHPO94TO"

def masking_spell(string):
    masked_code = ""
    length = len(string)
    index = length - 4
    vowels = ["A", "E", "I", "O", "U"]
    lastLetter = string[-1]

    if length < 8:
        print("Unstable code.")
    else:
        for i in range(0, index):
            masked_code += "*"
        for i in range(index, length):
            masked_code += string[i]

        if lastLetter in vowels:
            masked_code += " - Dark Magic Detected"

    return masked_code      

print(masking_spell(string1))
print(masking_spell(string2))
print(masking_spell(string3))

