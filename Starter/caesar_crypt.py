possible_directions = [["e", "en", "encrypt", "encryption"] , ["d", "de", "decrypt", "decryption"]]
possible_languages = [["r", "ru", "rus", "russian"], ["e", "en", "eng", "english"]]

# Encryption/decrtyption with Caesar cipher
def crypt_caesar(string, direction, alph, step):
    result = ""
    character_code = 0
    alphabet_length = alph[0]

    for c in string:
        if not c.isalpha():
            result += c
            continue
        
        character_code = ord(c.lower()) + direction * (step % alph[0])

        if not(alph[1] <= character_code <= alph[2]):
            character_code -= direction * alphabet_length
        
        if c.isupper():
            result += chr(character_code).upper()
        else:
            result += chr(character_code)
        
    return result

# Validate Encryption direction
def validate_direction(directions):
    inp = input("Enter crypt direction (encrypt/decrypt): ")

    while not (inp.lower() in directions[0] or inp.lower() in directions[1]):
        inp = input("ERROR: enter crypt direction again (encrypt/decrypt): ")

    if inp.lower() in directions[0]:
        return 1
    
    return -1

# Validate language selection
def validate_language(possible_languages):
    inp = input("Choose language (EN/RU): ")
    
    while not (inp.lower() in possible_languages[0] or inp.lower() in possible_languages[1]):
        inp = input("ERROR: enter language again (EN/RU): ")

    if inp.lower() in possible_languages[0]:
        return [32, ord('а'), ord('я')]
    
    return [26, ord('a'), ord('z')]

# validate step of encryption.
def validate_encryption_step():
    inp = input("Enter step of encryption/decryption: ")

    while not (inp.isnumeric() and int(inp) > 0):
        inp = input("ERROR: enter step of encryption/decryption again: ")

    return int(inp)

dir = validate_direction(possible_directions)
alpha = validate_language(possible_languages)
enc_step = validate_encryption_step()

print("Now, enter text you want to encrypt/decrypt:")
print(crypt_caesar(input(), dir, alpha, enc_step))