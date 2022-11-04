import string

def cipher(text,  key, characters = string.ascii_lowercase, decrypt=False):
    
    key = shift
    if key < 0:
        print("key cannot be negative")
        return None
    n = len(characters)
    if decrypt==True:
        key = n - key
    table = str.maketrans(characters, characters[key:]+characters[:key])
    translated_text = text.translate(table)
    return translated_text


from art import logo
print(logo)



should_end = False
while not should_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    print("\n")
    plain_text = input("Type your message:\n").lower()
    print("\n")
    shift = int(input("Type the shift number:\n"))
    print("\n")
    character_set = string.ascii_lowercase + string.digits + " "+ string.punctuation

    if direction == "encode":
        encrypted = cipher(plain_text, shift, character_set, decrypt=False)
        print("\n")
        print("Input text:\n",plain_text)
        print("\n")
        print("Encrypted text:\n",encrypted)
        print("\n")

    if direction == "decode":
        encrypted = cipher(plain_text, shift, character_set, decrypt=True)
        print("\n")
        print("Input text:\n",plain_text)
        print("\n")
        print("Encrypted text:\n",encrypted)
        print("\n")

    alphabet = character_set
    print("\n")
    restart = input("Type 'repeat' if you want to go again. Otherwise type 'exit'.\n")
    print("\n")
    if restart == "exit":
        should_end = True
        print("\n")
        print("Goodbye!")