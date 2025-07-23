# Password Entropy: E(in bits) = log2(N^L)
# where N is the pool of unique characters
# L = number of characters in your password
# checkout bitwarden.com/password-strength/ for estimated time to crack
# checkout timcutting.co.uk/tools/password-entropy

# Entropy of greater than 100 bits is extremely good

import math
import string

def password_entropy(str):

    max_lowercase = 26
    max_uppercase = 26
    max_numbers = 10
    special_chars = 29

    N = 0
    L = len(str)

    chars = list(str)
    upper_check = False
    lower_check = False
    num_check = False
    special_check = False

    # start of for loop
    for char in chars:
        if char in string.punctuation:
            special_check = True

        if char.isupper():
            upper_check = True
        
        if char.islower():
            lower_check = True
        
        if char.isnumeric():
            num_check = True
    # end of for loop

    if special_check:
        N += special_chars
    
    if upper_check:
        N += max_uppercase

    if lower_check:
        N += max_lowercase 
    
    if num_check:
        N += max_numbers
        
    return math.log2(N ** L)

print(f"Entropy (in bits): {password_entropy("qwerty")}")