# string1 = "AUC8EH"
# string2 = "ZY12QHPO94TR"
# string3 = "ZY12QHPO94TO"
strings = ["AUC8EH", "ZY12QHPO94TR", "ZY12QHPO94TO"]

def masking_spell(string):
    masked_code = ""
    length = len(string)
    index = length - 4
    vowels = "AEIOU"

    if length < 8:
        print("Unstable code.")
        
    else:
        for i in range(0, index):
            masked_code += "*"

        for i in range(index, length):
            masked_code += string[i]

        if string[-1] in vowels:
            masked_code += " - Dark Magic Detected"

    return masked_code      

for string in strings:
    print(masking_spell(string))