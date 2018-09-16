def encryption(text,key=0):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                chaar = ord(char)
                aplphabet = ((ord(char) - ord('a') - key) % 26) + ord('a')
            # if aplphabet > ord('z'):
            #     aplphabet -= 26
                newletter = chr(aplphabet)
                encrypted_text += "".join(newletter)
            else:
                chaar = ord(char)
                aplphabet = ((ord(char) - ord('A') - key) % 26) + ord('A')
            # if aplphabet > ord('z'):
            #     aplphabet -= 26
                newletter = chr(aplphabet)
                encrypted_text += "".join(newletter)            
        elif char == ' ':    
            encrypted_text += "".join(char)
    # table.append(newletter)
    return encrypted_text

def decryption(text,key=0):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                chaar = ord(char)
                aplphabet = ((ord(char) - ord('a') + key) % 26) + ord('a')
            # if aplphabet > ord('z'):
            #     aplphabet -= 26
                newletter = chr(aplphabet)
                decrypted_text += "".join(newletter)
            else:
                chaar = ord(char)
                aplphabet = ((ord(char) - ord('A') + key) % 26) + ord('A')
            # if aplphabet > ord('z'):
            #     aplphabet -= 26
                newletter = chr(aplphabet)
                decrypted_text += "".join(newletter)            
        elif char == ' ':    
            decrypted_text += "".join(char)
    # table.append(newletter)
    return decrypted_text

key = 1
text = 'Hello world'
print(encryption(text,key))
key = 1
text = 'Gdkkn vnqkc'
print(decryption(text,key))