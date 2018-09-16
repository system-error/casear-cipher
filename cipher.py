def encryption(text,key=0):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                aplphabet = ((ord(char) - ord('a') - key) % 26) + ord('a')
                newletter = chr(aplphabet)
                encrypted_text += "".join(newletter)
            else:
                aplphabet = ((ord(char) - ord('A') - key) % 26) + ord('A')
                newletter = chr(aplphabet)
                encrypted_text += "".join(newletter)            
        elif char == ' ':    
            encrypted_text += "".join(char)
    return encrypted_text

def decryption(text,key=0):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                aplphabet = ((ord(char) - ord('a') + key) % 26) + ord('a')
                newletter = chr(aplphabet)
                decrypted_text += "".join(newletter)
            else:
                aplphabet = ((ord(char) - ord('A') + key) % 26) + ord('A')
                newletter = chr(aplphabet)
                decrypted_text += "".join(newletter)            
        elif char == ' ':    
            decrypted_text += "".join(char)
    return decrypted_text

key = 1
text = 'Hello world'
print(encryption(text,key))
key = 1
text = 'Gdkkn vnqkc'
print(decryption(text,key))