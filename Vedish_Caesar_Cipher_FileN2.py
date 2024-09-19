import string

def caesar(text, shift, alphabets):

    def shift_alphabet(alphabet):
        return alphabet[shift:] + alphabet[:shift]

    shifted_alphabets = tuple(map(shift_alphabet, alphabets))
    final_alphabet = ''.join(alphabets)
    final_shifted_alphabet = ''.join(shifted_alphabets)
    table = str.maketrans(final_alphabet, final_shifted_alphabet)
    return text.translate(table)

plain_text = "This file is for @Prodigy_InfoTech!"
print(caesar(plain_text, 9, [string.ascii_lowercase, string.ascii_uppercase, string.punctuation]))    

#This is the First task assigned by Prodigy InfoTech to Vedish. Task has been completed. 
#In order to encrypt, just edit the following:  "This file is for @Prodigy_InfoTech!"
#In order to decrypt, just replace the following: 9 with -9 . 
#For Example: print(caesar(plain_text, 9, [string.ascii_lowercase, string.ascii_uppercase, string.punctuation])) 
#becomes print(caesar(plain_text, -9, [string.ascii_lowercase, string.ascii_uppercase, string.punctuation]))
