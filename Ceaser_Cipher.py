alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encrypt' to encrypt, type 'decrypt' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# def encrypt(text1, shift1):
#     c_text = ""
#     for char in text1:
#         print(char)
#         index = alphabet.index(char)
#         print(index)
#         new_index = index + shift
#         print(new_index)

#         if new_index > 25:
#             new_index = new_index - 26
#         new_char = alphabet[new_index]
#         c_text = c_text + new_char
    
#     print(f"The encrypted message is: {c_text}")

# def decrypt(text1, shift1):
#     c_text = ""
#     for char in text1:
#         print(char)
#         index = alphabet.index(char)
#         print(index)
#         new_index = index - shift
#         print(new_index)

#         if new_index < 0:
#             new_index = new_index + 26
#         new_char = alphabet[new_index]
#         c_text = c_text + new_char
    
#     print(f"The dencrypted message is: {c_text}")

# if direction == "encrypt":
#     encrypt(text, shift)

# if direction == "decrypt":
#     decrypt(text, shift)

def ceaser(text1, shift1, direction1):
    c_text = ""
    for char in text1:
        #print(char)
        index = alphabet.index(char)
        #print(index)
        
        if direction == "encrypt":
            new_index = index + shift
            if new_index > 25:
                new_index = new_index - 26
        if direction == "decrypt":
            new_index = index - shift
            if new_index < 0:
                new_index = new_index + 26
        
        new_char = alphabet[new_index]
        c_text = c_text + new_char
    print(f"The result is: {c_text}")

ceaser(text, shift, direction)